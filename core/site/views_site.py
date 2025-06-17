from django.shortcuts import render,redirect

def index(request):
    ctx = {}
    return render(request,'site/index.html',ctx)

def cargo(request):
    ctx = {}
    return render(request,'site/cargo-details.html',ctx)

def delivery(request):
    ctx = {}
    return render(request,'site/delivery-details.html',ctx)

def taxi(request):
    ctx = {}
    return render(request,'site/taxi-details.html',ctx)

