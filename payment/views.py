import stripe
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView

from order.models import Order
from payment.banks.bankfactories import BankFactory
from payment.banks.stripe import Stripe
from payment.banks.zibal import Zibal


class RequestPaymentApi(APIView):
    class InputSerializer(serializers.Serializer):
        bank_type = serializers.CharField(required=False)
        order_id = serializers.IntegerField(required=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order.objects.get(id=serializer.data["order_id"])
        factory = BankFactory()
        if "bank_type" in serializer.data:
            bank_type = serializer.data["bank_type"]
        else:
            bank_type = "None"
        bank = factory.create(bank_type)
        bank.set_request(request)
        bank._gateway_amount = int(order.amount)
        bank._order = order
        bank.ready()
        data = {"gateway_url": bank.get_gateway_payment_url()}
        return Response(data)


class RequestPaymentVerifyApi(APIView):
    def get(self, request, *args, **kwargs):
        data = self.request.query_params
        get_data = {}
        for i in data:
            get_data[i] = data.get(i)
        get_data["bank_type"] = kwargs["bank_type"]
        return self.post(request, get_data)

    def post(self, request, *args, **kwargs):
        # اگر فقط با متد پست از سمت بانگ بیاد به مشکل میخوریم؟؟ اینو چطور هندل کینیم TODO
        print(args, kwargs)
        factory = BankFactory()
        bank = factory.create(args[0]["bank_type"])
        post_data = self.request.data
        post_data.update(args[0])
        data = {"verify_result": bank.verify(post_data)}
        return Response(data)
