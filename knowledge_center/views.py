from django.shortcuts import render
from .models import *

# Create your views here.
def show_categories(request):
    return render(request, "categories.html", {'categories': Category.objects.all()})