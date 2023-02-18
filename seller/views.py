from django.shortcuts import render
from .models import *

# Create your views here.
def seller_index(request):
    try:
        s_obj = Seller.objects.get(email = request.session['seller_email'])
        return render(request, 'seller_index.html', {'seller_data': s_obj})
    except:
        return render(request, 'seller_login.html')

def seller_login(request):
    if request.method == 'GET':
        return render(request, 'seller_login.html')
    else:
        try:
            s_obj = Seller.objects.get(email = request.POST['email'])
            if request.POST['password'] == s_obj.password:
                request.session['seller_email'] = request.POST['email']
                return render(request, 'seller_index.html', {'seller_data': s_obj})

        except:
            return render(request, 'seller_login.html', {"msg": 'Email Is Not Registered!!'})
        
    
def seller_logout(request):
    del request.session['seller_email']
    return render(request, 'seller_login.html')


def add_product(request):
    if request.method == 'GET':
        return render(request, 'add_product.html')
    else:
        Product.objects.create(
            product_name = request.POST['product_name'],
            des = request.POST['des'],
            price = request.POST['price'],
            product_stock = request.POST['product_stock'],
            pic = request.FILES['pic']
        )
        return render(request, 'add_product.html', {'msg': 'Product Successfully Added!'})
