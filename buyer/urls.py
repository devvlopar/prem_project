from django.urls import path
from .views import * 

urlpatterns = [ 
    path('index/', index, name="index"),
    path('prem/', fun1, name="fun1"),
    
]