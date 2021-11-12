from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView

from payment.banks.bankfactories import BankFactory
from payment.banks.zibal import Zibal


class RequestPaymentApi(APIView):
    class InputSerializer(serializers.Serializer):
        amount = serializers.FloatField()
        bank_type = serializers.CharField(required=False)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        factory = BankFactory()
        if "bank_type" in serializer.data:
            bank_type = serializer.data["bank_type"]
        else:
            bank_type = "None"
        bank = factory.create(bank_type)
        bank.set_request(request)
        bank._gateway_amount = int(serializer.data["amount"])
        bank.ready()
        data = {"gateway_url": bank.get_gateway_payment_url()}
        return Response(data)


class RequestPaymentVerifyApi(APIView):
    def get(self, request):
        data = self.request.query_params
        get_data = {}
        for i in data:
            get_data[i] = data.get(i)
        return self.post(request, get_data)

    def post(self, request, get_data):
        bank = Zibal()
        post_data = self.request.data
        post_data.update(get_data)
        data = {"verify_result": bank.verify(post_data)}
        return Response(data)
