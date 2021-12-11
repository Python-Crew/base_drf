from django.contrib import admin
from order.models import Order, OrderLine


class OrderLineInline(admin.StackedInline):
    model = OrderLine
    can_delete = True
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderLineInline,
    ]


admin.site.register(Order, OrderAdmin)
