import importlib

from payment.banks.banks import BaseBank
import requests
from django.conf import settings

from payment.models import PaymentRecord

if getattr(settings, "BANK_TYPE", None) is not None:
    package, attr = settings.BANK_TYPE.rsplit(".", 1)
    BankType = getattr(importlib.import_module(package), attr)
else:
    from payment.banks.paymentstatuses import BankType


if getattr(settings, "PAYMENT_STATUSES", None) is not None:
    package, attr = settings.PAYMENT_STATUSES.rsplit(".", 1)
    PaymentStatus = getattr(importlib.import_module(package), attr)
else:
    from payment.banks.paymentstatuses import PaymentStatus


class Zibal(BaseBank):
    _bank_config = getattr(settings, "BANK_SETTINGS", None)

    def __init__(self, **kwargs):
        super(Zibal, self).__init__(**kwargs)
        self._merchant_code = self._bank_config["zibal"]["merchant_code"]
        self._token_api_url = self._bank_config["zibal"]["token_api_url"]
        self._payment_url = self._bank_config["zibal"]["payment_url"]
        self._verify_api_url = self._bank_config["zibal"]["verify_api_url"]

    def get_bank_type(self):
        return BankType.ZIBAL

    def _get_gateway_payment_url_parameter(self):
        return self._payment_url.format(self._transaction_code)

    def _get_gateway_payment_parameter(self):
        """اطلاعات سفارش و .... میشه اینجا فرستاد"""
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
        print(data, "sf")
        return data

    def pay(self):
        super(Zibal, self).pay()
        data = self.get_pay_data()
        response_json = self._send_data(self._token_api_url, data)
        if response_json["result"] == 100:
            self._transaction_code = response_json["trackId"]
            self._payment_record.transaction_code = self._transaction_code
            self._payment_record.status = PaymentStatus.REDIRECT_TO_BANK

        else:
            self._payment_record.status = PaymentStatus.FAILED
            pass
        self._payment_record.response_result = response_json["result"]
        self._payment_record.extra_information = response_json
        self._payment_record.save()

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
            self._payment_record.extra_information = response_json
            self._payment_record.response_result = response_json["result"]
        elif response_json["result"] is not 100 and 201:
            self._payment_record.status = PaymentStatus.CANCEL_BY_USER
            self._payment_record.extra_information = response_json
            self._payment_record.response_result = response_json["result"]
        self._payment_record.save()
        return response_json

    def _send_data(self, api, data):
        try:
            response = requests.post(url=api, json=data)

        except Exception as e:
            print(e)
        response_json = response.json()
        return response_json
