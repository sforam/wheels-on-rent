from django.shortcuts import render,redirect

# Create your views here.


def dashboard(request):
    return render(request,"host/index.html")

def sidebar(request):
    return render(request,"host/sidebar.html")

def addpayment(request):
    return render(request,"host/addpayment.html")

def login(request):
    return render(request,"host/login.html")

def forgot_password(request):
    return render(request,"host/forgot_password.html")


def signup(request):
    return render(request,"host/signup.html")


def twowheeler(request):
    return render(request,"host/2wheeler.html")

def addtwowheeler(request):
    return render(request,"host/add2wheeler.html")



def tables(request):
    return render(request,"host/tables.html")
