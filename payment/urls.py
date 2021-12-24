from django.urls import path
from payment.views import RequestPaymentApi, RequestPaymentVerifyApi

urlpatterns = [
    path(
        "request_payment/create/",
        RequestPaymentApi.as_view(),
        name="payment_request_create",
    ),
    path(
        "request_payment/verify/<str:bank_type>/",
        RequestPaymentVerifyApi.as_view(),
        name="payment_request_verify",
    ),
]
