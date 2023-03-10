from django.urls import path
from .views import * 

urlpatterns = [ 
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('create_row/', create_row, name="create_row"),
    path('delete_row/', delete_row, name="delete_row"),
    path('faqs/', faqs, name="faqs"),
    path('cart/', cart, name="cart"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),    
    path('logout/', logout, name="logout"),
    path('edit_profile/', edit_profile, name="edit_profile"),
    path('forgot_password/', forgot_password, name="forgot_password"),
    path('add_to_cart/<int:pk>', add_to_cart, name="add_to_cart"),
    path('del_cart_item/<int:cart_id>', del_cart_item, name="del_cart_item"),





]