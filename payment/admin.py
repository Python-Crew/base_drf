from django.contrib import admin

# Register your models here.
from payment.models import PaymentRecord

admin.site.register(PaymentRecord)
