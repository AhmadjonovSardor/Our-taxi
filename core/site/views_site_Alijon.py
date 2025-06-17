from django.shortcuts import render, redirect





def index(request):
    ctx = {}
    return render(request, "site/index.html", ctx)

def cargo(request):
    ctx = {}
    return render(request, "site/index.html", ctx)