from django.shortcuts import render,redirect

# Create your views here.


def dashboard(request):
    return render(request,"admin/index.html")

def sidebar(request):
    return render(request,"admin/sidebar.html")

def addpayment(request):
    return render(request,"admin/addpayment.html")

def login(request):
    return render(request,"admin/login.html")

def twowheeler(request):
    return render(request,"admin/2wheeler.html")

def addtwowheeler(request):
    return render(request,"admin/add2wheeler.html")



def tables(request):
    return render(request,"admin/tables.html")
