from abc import ABC, abstractmethod
from datetime import datetime
import json
from django.shortcuts import redirect
from django.urls import reverse
from prices import Money
import requests
from urllib import parse

from zibal import zibal


def append_querystring(url: str, params: dict) -> str:
    url_parts = list(parse.urlparse(url))
    query = dict(parse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = parse.urlencode(query)

    return parse.urlunparse(url_parts)


class BaseBank(ABC):
    """Base bank for sending to gateway."""

    _gateway_currency: str = ""
    _currency: ""
    _gateway_amount: int = 0
    _transaction_status_text = "status"
    _request = None
    _tracking_code: 123
    _transaction_code: str = None
    _callback_url = "http://127.0.0.1:8000/payment/request_payment/verify/"

    def set_request(self, request):
        """اینجا تایپ ریکوست هر بانک رو میگیره"""
        self._request = request

    def get_gateway_amount(self):
        return self._gateway_amount

    @abstractmethod
    def get_pay_data(self):
        pass

    @abstractmethod
    def get_verify_data(self):
        pass

    @abstractmethod
    def verify(self, params):
        pass

    @abstractmethod
    def pay(self):
        pass

    def _set_transaction_status_text(self, txt):
        self._transaction_status_text = txt

    @abstractmethod
    def _get_gateway_payment_method_parameter(self):
        pass

    @abstractmethod
    def _get_gateway_payment_parameter(self):
        pass

    def _get_gateway_payment_url_parameter(self):
        pass

    def ready(self):
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


class Zibal(BaseBank):
    _merchant_code = "zibal"
    _transaction_code = None

    def __init__(self, **kwargs):
        super(Zibal, self).__init__(**kwargs)
        self._token_api_url = "https://gateway.zibal.ir/v1/request"
        self._payment_url = "https://gateway.zibal.ir/start/{}"
        self._verify_api_url = "https://gateway.zibal.ir/v1/verify"

    def _get_gateway_payment_url_parameter(self):
        return self._payment_url.format(self._transaction_code)

    def _get_gateway_payment_parameter(self):
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

    def get_verify_data(self):
        pass

    def verify(self, params):
        super(Zibal, self).verify(params)
        data = {
            "merchant": self._merchant_code,
            "trackId": params.get("trackId"),
        }
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
        self._set_transaction_status_text(response_json["message"])
        return response_json
