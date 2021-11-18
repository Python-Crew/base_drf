from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import path
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils.html import format_html
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
