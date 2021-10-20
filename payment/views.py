from django import forms
from django.shortcuts import render

# Create your views here.
import zibal.zibal as zibal

import logging

from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import serializers

from payment.banks.banks import Zibal
from rest_framework.views import APIView


class RequestPaymentApi(APIView):
    class InputSerializer(serializers.Serializer):
        amount = serializers.FloatField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bank = Zibal()
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
