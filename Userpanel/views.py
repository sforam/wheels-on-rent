from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages #import messages


import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='wheels_on_rent')
print('Successfully connected to database')
cur = conn.cursor()



# Create your views here.

def sidebar(request):
    return render(request,"user/sidebar.html")

def home(request):
    return render(request,"user/index.html")

def car(request):
    return render(request,"user/car.html")

def cardetails(request):
    return render(request,"user/cardetails.html")


def payment(request):
    return render(request,"user/payment.html")

def login(request):
    return render(request,"user/login.html")

def forgot_password(request):
    return render(request,"user/forgot_password.html")


#----------------------------------------------signup page---------------------------------------------------------
def signup(request):
    return render(request,"user/signup.html")

def signupaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        Full_Name = request.POST['nm']
        Email = request.POST['em']
        Mobile_No = request.POST['cn']
       
        Gender = request.POST['user_gender']
        Password = request.POST['pwd']
        
        cur.execute("INSERT INTO `user_table`(`Full_Name`,`Email`,`Mobile_No`,`Gender`,`Password`) VALUES ('{}','{}','{}','{}','{}')".format(Full_Name,Email,Mobile_No,Gender,Password))
        conn.commit()
        messages.success(request, 'Signup Details added successfully')
   
        return redirect(signup) 
    else:
        return redirect(signup)
  
  

def twowheeler(request):
    return render(request,"user/2wheeler.html")

def about(request):
    return render(request,"user/about.html")


def feedback(request):
    return render(request,"user/feedback.html")
