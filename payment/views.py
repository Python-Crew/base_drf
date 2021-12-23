from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from order.models import Order
from payment.services import gateway_payment_request, gateway_verify_payment_request

from payment.banks.bankfactories import BankFactory
from payment.banks.zibal import Zibal


class RequestPaymentApi(APIView):
    class InputSerializer(serializers.Serializer):
        bank_type = serializers.CharField(required=False)
        order_id = serializers.IntegerField(required=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order.objects.get(id=serializer.data["order_id"])
        bank_type = serializer.data["bank_type"]
        data = gateway_payment_request(request, order, bank_type)
        return Response(data)


class RequestPaymentVerifyApi(APIView):
    def get(self, request, bank_type, *args, **kwargs):
        return self.post(request, bank_type, *args, **kwargs)

    def post(self, request, bank_type, *args, **kwargs):
        data = gateway_verify_payment_request(request, bank_type)
        return Response(data)
