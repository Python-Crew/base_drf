from django.urls import path, include
from rest_framework.routers import DefaultRouter

from payment.views import RequestPaymentApi, RequestPaymentVerifyApi

urlpatterns = [
    path(
        "request_payment/create/",
        RequestPaymentApi.as_view(),
        name="payment_request_create",
    ),
    path(
        "request_payment/verify/",
        RequestPaymentVerifyApi.as_view(),
        name="payment_request_verify",
    ),
]
