from abc import ABC, abstractmethod
from django.shortcuts import redirect
from urllib import parse
import BaseDRF.settings as settings
from order.models import Order
from payment.models import PaymentRecord


def append_querystring(url: str, params: dict) -> str:
    url_parts = list(parse.urlparse(url))
    query = dict(parse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = parse.urlencode(query)
    return parse.urlunparse(url_parts)


class BaseBank(ABC):
    """Base bank for sending to gateway."""

    _gateway_amount: int = 0
    _request: str = None
    _transaction_code: str = ""
    _callback_url = settings.CALLBACK_URL
    _order = Order = None
    _payment_record: PaymentRecord = None
    _response_result: str = None

    def set_request(self, request):
        """اینجا تایپ ریکوست هر بانک رو میگیره"""
        self._request = request

    @abstractmethod
    def callback_url(self, request):
        pass

    @abstractmethod
    def get_bank_type(self):
        pass

    def get_gateway_amount(self):
        return self._gateway_amount

    @abstractmethod
    def get_pay_data(self):
        pass

    @abstractmethod
    def verify(self, params):
        pass

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def _get_gateway_payment_method_parameter(self):
        pass

    @abstractmethod
    def _get_gateway_payment_parameter(self):
        pass

    def _get_gateway_payment_url_parameter(self):
        pass

    def ready(self):
        payment_record = PaymentRecord.objects.create(
            order=self._order,
            bank_type=self.get_bank_type(),
            amount=self.get_gateway_amount(),
            transaction_code=self._transaction_code,
            response_result=self._response_result,
            callback_url=self.callback_url,
        )
        print(payment_record)
        self._payment_record = payment_record
        self.pay()

    def redirect_gateway(self):
        """کاربر را به درگاه بانک هدایت می کند"""
        return redirect(self.get_gateway_payment_url())

    def get_gateway_payment_url(self):
        url = self._get_gateway_payment_url_parameter()
        params = self._get_gateway_payment_parameter()
        method = self._get_gateway_payment_method_parameter()
        params.update(
            {
                "method": method,
            }
        )
        redirect_url = append_querystring(url, params)
        if self._request:
            redirect_url = self._request.build_absolute_uri(redirect_url)
        return redirect_url
