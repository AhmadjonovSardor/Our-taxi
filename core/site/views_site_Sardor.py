from django.shortcuts import render,redirect

def delivery(request):
    ctx = {}
    return render(request,'site/delivery-details.html',ctx)

def taxi(request):
    ctx = {}
    return render(request,'site/taxi-details.html',ctx)

