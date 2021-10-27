from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView

from payment.banks.bankfactories import BankFactory
from payment.banks.zibal import Zibal


class RequestPaymentApi(APIView):
    class InputSerializer(serializers.Serializer):
        amount = serializers.FloatField()
        bank_type = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bank_type = serializer.data["bank_type"]
        factory = BankFactory()
        bank = factory.create(bank_type)
        bank.set_request(request)
        bank._gateway_amount = int(serializer.data["amount"])
        bank.ready()
        data = {"gateway_url": bank.get_gateway_payment_url()}
        return Response(data)


class RequestPaymentVerifyApi(APIView):
    def get(self, request):
        bank = Zibal()
        data = {"verify_result": bank.verify(self.request.query_params)}
        return Response(data)

    def post(self, request):
        bank = Zibal()
        data = {"verify_result": bank.verify(self.request.query_params)}
        return Response(data)
