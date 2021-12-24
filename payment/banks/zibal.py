from order.orderstatuses import OrderStatus, CurrencyEnum
from payment.banks.banks import BaseBank
import requests
from django.conf import settings
from payment.models import PaymentRecord
from payment.banks.paymentstatuses import BankType
from payment.banks.paymentstatuses import PaymentStatus


class Zibal(BaseBank):
    _bank_config = getattr(settings, "BANK_SETTINGS", None)

    def __init__(self, **kwargs):
        super(Zibal, self).__init__(**kwargs)
        self._merchant_code = self._bank_config["zibal"]["merchant_code"]
        self._token_api_url = self._bank_config["zibal"]["token_api_url"]
        self._payment_url = self._bank_config["zibal"]["payment_url"]
        self._verify_api_url = self._bank_config["zibal"]["verify_api_url"]
        self._callback_url = settings.CALLBACK_URL + "Zibal/"

    def callback_url(self, request):
        return self._callback_url

    def get_bank_type(self):
        return BankType.ZIBAL

    def valid_currency(self):
        return ["CAD", "USD"]

    def _get_gateway_payment_url_parameter(self):
        return self._payment_url.format(self._transaction_code)

    def _get_gateway_payment_parameter(self):
        params = {"order": self._order.id}
        return params

    def _get_gateway_payment_method_parameter(self):
        return "GET"

    def get_pay_data(self):
        data = {
            "merchant": self._merchant_code,
            "amount": self.get_gateway_amount(),
            "callbackUrl": self._callback_url,
            "order": self._order.id,
        }
        return data

    def pay(self):
        super(Zibal, self).pay()
        data = self.get_pay_data()
        response_json = self._send_data(self._token_api_url, data)
        if response_json["result"] == 100:
            self._transaction_code = response_json["trackId"]
            self._payment_record.transaction_code = self._transaction_code
            self._payment_record.status = PaymentStatus.REDIRECT_TO_BANK
            self._payment_record.order.status = OrderStatus.WAITING_FOR_PAYMENT

        else:
            self._payment_record.status = PaymentStatus.FAILED
            self._payment_record.order.status = OrderStatus.FAILED_PAYMENT

        self._payment_record.response_result = response_json["result"]
        self._payment_record.extra_information = response_json
        self._payment_record.save()
        self._payment_record.order.save()

    def verify(self, params):
        super(Zibal, self).verify(params)
        data = {
            "merchant": self._merchant_code,
            "trackId": params.get("trackId"),
        }
        self._payment_record = PaymentRecord.objects.get(
            transaction_code=data["trackId"]
        )

        response_json = self._send_data(self._verify_api_url, data)
        if response_json["result"] == 100 and response_json["status"] == 1:
            self._payment_record.status = PaymentStatus.COMPLETE
            self._payment_record.order.status = OrderStatus.PAID

        elif response_json["result"] != 100 and 201:
            self._payment_record.status = PaymentStatus.CANCEL_BY_USER
            self._payment_record.order.status = OrderStatus.FAILED_PAYMENT

        self._payment_record.extra_information = response_json
        self._payment_record.response_result = response_json["result"]
        self._payment_record.save()
        self._payment_record.order.save()
        return self._payment_record.status

    def _send_data(self, api, data):
        try:
            response = requests.post(url=api, json=data)

        except Exception as e:
            print(e)
        response_json = response.json()
        return response_json
