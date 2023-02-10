from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    try:
        user_obj = Buyer.objects.get(email = request.session['buyer_email'])
        return render(request, 'index.html', {'user_data': user_obj })

    except:
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

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        try:
            user_obj = Buyer.objects.get(email = request.POST['email'])
            return render(request, 'register.html',{'msg': 'Email Already Exists'})
        except:
            return HttpResponse('OTP bhejunga')


def otp(request):

        Buyer.objects.create(
            #POST['first_name'] : ye key register.html ke form mein
            #  <input> tag mein name="first_name"
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        return render(request, 'register.html', {"mprr":'Created Successfully'})

def cart(request):
    return render(request, 'cart.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            user_obj = Buyer.objects.get(email = request.POST['email'])
            if request.POST['password'] == user_obj.password:
                #nayi key value pair de rha hu
                request.session['buyer_email'] = request.POST['email']
                return render(request, 'index.html', {'user_data':user_obj})
        except:
            return render(request, 'login.html', {'msg': 'Email Is Not Registered!!'})


def logout(request):
    pass