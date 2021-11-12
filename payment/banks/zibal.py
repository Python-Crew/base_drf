from BaseDRF.settings import BANK_SETTINGS
from payment.banks.banks import BaseBank
import requests
from django.conf import settings


class Zibal(BaseBank):
    _bank_config = getattr(settings, 'BANK_SETTINGS', None)

    def __init__(self, **kwargs):
        super(Zibal, self).__init__(**kwargs)
        self._merchant_code = self._bank_config['zibal']["merchant_code"]
        self._token_api_url = self._bank_config["zibal"]["token_api_url"]
        self._payment_url = self._bank_config["zibal"]["payment_url"]
        self._verify_api_url = self._bank_config["zibal"]["verify_api_url"]

    def _get_gateway_payment_url_parameter(self):
        return self._payment_url.format(self._transaction_code)

    def _get_gateway_payment_parameter(self):
        """اطلاعات سفارش و .... میشه اینجا فرستاد"""
        params = {}
        return params

    def _get_gateway_payment_method_parameter(self):
        return "GET"

    def get_pay_data(self):
        data = {
            "merchant": self._merchant_code,
            "amount": self.get_gateway_amount(),
            "callbackUrl": self._callback_url,
        }
        return data

    def pay(self):
        super(Zibal, self).pay()
        data = self.get_pay_data()
        response_json = self._send_data(self._token_api_url, data)
        if response_json["result"] == 100:
            self._transaction_code = response_json["trackId"]
        else:
            pass

    def verify(self, params):
        super(Zibal, self).verify(params)
        data = {
            "merchant": self._merchant_code,
            "trackId": params.get("trackId"),
        }
        print(data)
        response_json = self._send_data(self._verify_api_url, data)
        if response_json["result"] == 100 and response_json["status"] == 1:
            print(response_json["result"])
        else:
            print(response_json["result"])
        return response_json

    def _send_data(self, api, data):
        try:
            response = requests.post(url=api, json=data)

        except Exception as e:
            print(e)
        response_json = response.json()
        return response_json
