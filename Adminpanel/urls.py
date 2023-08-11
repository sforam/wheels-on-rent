#from django.contrib import admin

from django.urls import path
from .import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('sidebar', views.sidebar, name='sidebar'),
    path('twowheeler', views.twowheeler, name='twowheeler'),
    path('addtwowheeler', views.addtwowheeler, name='addtwowheeler'),
    path('addpayment', views.addpayment, name='addpayment'),
    path('login', views.login, name='login'),
    
   
    path('tables', views.tables, name='tables'),
    

]
