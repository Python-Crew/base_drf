from django import forms
from django.shortcuts import render

# Create your views here.
import zibal.zibal as zibal

import logging

from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from payment.banks.banks import Zibal


class PaymentSampleForm(forms.Form):
    amount = forms.IntegerField(label='Amount', initial=10000)

def sample_payment_view(request):
    if request.method == 'POST':
        form = PaymentSampleForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            try:
                bank = Zibal()
                bank.set_request(request)
                bank._gateway_amount = int(amount)
                bank._callback_url = 'http://127.0.0.1:8000/sample-result/'
                bank.ready()
                return bank.redirect_gateway()
            except Exception as e:
                print(e, 'Exception in payment view')
                raise e

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PaymentSampleForm()

    return render(request, 'samples/gateway.html', {'form': form})


def sample_result_view(request):
    if int(request.GET.get('success')) == 1:
        massage = True

    if int(request.GET.get('success')) == 0:
        massage = False
    context = {
        'massage' : massage
    }

    return render(request, 'samples/result.html', context)
