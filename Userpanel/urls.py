#from django.contrib import admin

from turtle import home
from django.urls import path 
from . import views 

urlpatterns = [
    path('home', views.home, name='home'),
    path('sidebar', views.sidebar, name='sidebar'),
    path('car', views.car, name='car'),
    path('cardetails', views.cardetails, name='cardetails'),
  
    path('login', views.login, name='login'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    
    path('signup', views.signup, name="signup"),
    path('signup/inserted', views.signupaddprocess, name="signupaddprocess"),
   
    path('2wheeler', views.twowheeler, name='2wheeler'),
    path('about', views.about, name='about'),
    path('payment', views.payment, name='payment'),
    



    path('feedback', views.feedback, name='feedback'),
    
    

]
