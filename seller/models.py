from django.db import models

# Create your models here.
class Seller(models.Model):
    full_name = models.CharField(max_length= 50)
    gst_no = models.CharField(max_length= 50)
    address = models.CharField(max_length= 50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    pic = models.FileField(upload_to='seller_pics', default='sad.jpeg')

    
    def __str__(self):
        return self.full_name
    

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    des = models.CharField(max_length=100)
    price = models.FloatField(default=10.0)
    product_stock = models.IntegerField(default=0)
    pic = models.FileField(upload_to='product_pics', default='sad.jpeg')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name
