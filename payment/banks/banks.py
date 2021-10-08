from abc import ABC, abstractmethod
from datetime import datetime
import json
from django.shortcuts import redirect
from prices import Money
import requests


def get_json(resp):
    """
    :param response:returned response as json when sending a request
    using 'requests' module.

    :return:response's content with json format
    """

    return json.loads(resp.content.decode('utf-8'))


class BaseBank(ABC):
    """Base bank for sending to gateway."""
    _gateway_currency: str = ''
    _currency: ''
    _gateway_amount: int = 0
    _callback_url = 'www'
    _transaction_status_text = 'status'


    def set_request(self, request):
        """اینجا تایپ ریکوست هر بانک رو میگیره"""
        self._request = request

    def get_gateway_amount(self):
        return self._gateway_amount

    def redirect_client_callback(self):
        """"ریدایرکت بعد از برگشت از سمت درگاه بانک"""
        return redirect(self._callback_url)

    @abstractmethod
    def get_pay_data(self):
        pass

    @abstractmethod
    def pay(self):
        pass

    def _set_transaction_status_text(self, txt):
        self._transaction_status_text = txt

    # TODO حالا پروسه ریدایرکت شده به بانک باید اینجا انجام بشه


class BMI(BaseBank):
    _merchant_code = None

    def __init__(self, **kwargs):
        super(BMI, self).__init__(**kwargs)
        self._token_api_url = 'https://sadad.shaparak.ir/vpg/api/v0/Request/PaymentRequest'
        self._payment_url = "https://sadad.shaparak.ir/VPG/Purchase"
        self._verify_api_url = 'https://sadad.shaparak.ir/vpg/api/v0/Advice/Verify'

    def get_pay_data(self):
        data = {
            'MerchantId': self._merchant_code,
            'Amount': self.get_gateway_amount(),  # base
            'RedirectURL': self._callback_url,  # base
        }
        return data

    def _get_gateway_payment_method_parameter(self):
        return "GET"

    def pay(self):
        super(BMI, self).pay()
        data = self.get_pay_data()
        response_json = self._send_data(self._token_api_url, data)
        if response_json['ResCode'] == '0':
            " success"
            pass
        else:
            raise self._transaction_status_text

    def _send_data(self, api, data):
        try:
            response = requests.post(api, json=data, timeout=5)
        except requests.Timeout:
            raise Exception
        except requests.ConnectionError:
            raise Exception

        response_json = get_json(response)
        self._set_transaction_status_text(response_json['Description'])
        return response_json



class SEP(BaseBank):
    _merchant_code = None

    def __init__(self, **kwargs):
        super(SEP, self).__init__(**kwargs)
        self._token_api_url = 'https://sep.shaparak.ir/MobilePG/MobilePayment'
        self._payment_url = 'https://sep.shaparak.ir/OnlinePG/OnlinePG'
        self._verify_api_url = 'https://verify.sep.ir/Payments/ReferencePayment.asmx?WSDL'

    def get_pay_data(self):
        data = {
            'Action': 'Token',
            'Amount': self.get_gateway_amount(),  # base
            'Wage': 0,
            'TerminalId': self._merchant_code,    # here
            'RedirectURL': self._callback_url,  # base
        }
        return data


    def _get_gateway_payment_method_parameter(self):
        return 'POST'

    def pay(self):
        super(SEP, self).pay()
        data = self.get_pay_data()
        response_json = self._send_data(self._token_api_url, data)
        if str(response_json['status']) == '1':
            """ موفق بوده"""
            pass
        else:
            raise self._transaction_status_text

    def _send_data(self, api, data):
        try:
            response = requests.post(api, json=data, timeout=5)
        except requests.Timeout:
            raise Exception
        except requests.ConnectionError:
            raise Exception

        response_json = get_json(response)
        self._set_transaction_status_text(response_json.get('errorDesc'))
        return response_json


class Zibal(BaseBank):
    _merchant_code = None

    def __init__(self, **kwargs):
        super(Zibal, self).__init__(**kwargs)
        self._token_api_url = 'https://gateway.zibal.ir/v1/request'
        self._payment_url = 'https://gateway.zibal.ir/start/{}'
        self._verify_api_url = 'https://gateway.zibal.ir/v1/verify'


    def _get_gateway_payment_method_parameter(self):
        return "GET"

    def get_pay_data(self):
        data = {
            'merchant': self._merchant_code,
            'amount': self.get_gateway_amount(),
            'callbackUrl': self._callback_url,  # base
        }
        return data

    def pay(self):
        super(Zibal, self).pay()
        data = self.get_pay_data()
        response_json = self._send_data(self._token_api_url, data)
        if response_json['result'] == 100:
            """ موفق بوده"""
            pass
        else:
            raise self._transaction_status_text

    def _send_data(self, api, data):
        try:
            response = requests.post(api, json=data, timeout=5)
        except requests.Timeout:
            raise Exception
        except requests.ConnectionError:
            raise Exception

        response_json = get_json(response)
        self._set_transaction_status_text(response_json['message'])
        return response_json
