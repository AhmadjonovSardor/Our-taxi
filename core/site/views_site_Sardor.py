from django.shortcuts import render,redirect
from core.models.models_site_Sardor import CarDelivery,CarTaxi,CarDeliveryType,CarTaxiType


def delivery(request):

    ctx = {}
    return render(request,'site/delivery-details.html',ctx)



def taxi(request):
    ctx = {}
    return render(request,'site/taxi-details.html',ctx)

