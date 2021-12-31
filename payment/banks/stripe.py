from abc import ABC
from payment.banks.banks import BaseBank
from django.conf import settings
from payment.models import PaymentRecord
from payment.banks.paymentstatuses import BankType
from payment.banks.paymentstatuses import PaymentStatus
from order.orderstatuses import OrderStatus
import stripe


class Stripe(BaseBank, ABC):
    _bank_config = getattr(settings, "BANK_SETTINGS", None)

    def __init__(self, **kwargs):
        super(Stripe, self).__init__(**kwargs)
        self._payment_url = None
        self._api_key = self._bank_config["stripe"]["api_key"]

    def callback_url(self, request):
        return settings.CALLBACK_URL

    def get_bank_type(self):
        return BankType.STRIPE

    def valid_currency(self):
        return ["CAD", "USD"]

    def _get_gateway_payment_url_parameter(self):
        return self._payment_url

    def _get_gateway_payment_parameter(self):
        params = {}
        return params

    def _get_gateway_payment_method_parameter(self):
        return "GET"

    def get_pay_data(self):
        data = {}
        return data

    def pay(self):
        super(Stripe, self).pay()
        stripe.api_key = self._api_key
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": self._order.currency,
                        "unit_amount": int(self._payment_record.amount * 100),
                        "product_data": {
                            "name": self._order.user.username,
                        },
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=self._callback_url + "Stripe/?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=self._callback_url + "Stripe/?session_id={CHECKOUT_SESSION_ID}",
        )
        # for PaymentRecord
        self._payment_record.status = PaymentStatus.REDIRECT_TO_BANK
        self._payment_record.transaction_code = checkout_session.id
        self._payment_record.extra_information = checkout_session
        self._payment_record.save()

        # for Order
        self._payment_record.order.status = OrderStatus.WAITING_FOR_PAYMENT
        self._payment_record.order.save()

        self._payment_url = checkout_session.url

    def verify(self, params):
        super(Stripe, self).verify(params)
        stripe.api_key = self._api_key
        self._payment_record = PaymentRecord.objects.get(
            transaction_code=params["session_id"]
        )
        session = stripe.checkout.Session.retrieve(params["session_id"])
        if session.payment_status == "paid":
            self._payment_record.status = PaymentStatus.COMPLETE
            self._payment_record.order.status = OrderStatus.PAID
        else:
            self._payment_record.status = PaymentStatus.CANCEL_BY_USER
            self._payment_record.order.status = OrderStatus.FAILED_PAYMENT

        self._payment_record.extra_information = session
        self._payment_record.response_result = session.payment_status
        self._payment_record.save()
        self._payment_record.order.save()

        return self._payment_record.status
