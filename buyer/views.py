from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def fun1(request):
    return HttpResponse('ye prem ka response hai')

def create_row(request):
    Buyer.objects.create(
        first_name = 'devang',
        last_name = 'singh',
        email = 'dev@gmail.com',
        password = 'prem1234',
        address = '176, vishnunagar, udhna, surat',
        gender = 'yudasg'
    )
    return HttpResponse('row create ho gaya')

def delete_row(request):
    d_row = Buyer.objects.get(email = 'pre@gmail.com')
    d_row.delete()
    return HttpResponse('delete ho gya')

def faqs(request):
    return render(request, 'faqs.html')