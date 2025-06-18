from django.shortcuts import render, redirect


def index(request):
    ctx = {}
    if request.GET.get("service") == "delivery":
        ctx["from"] = request.GET.get("from")
        ctx["to"] = request.GET.get("to")
        return render(request, 'site/delivery-details.html', ctx)

    if request.GET.get("service") == "cargo":
        ctx["from"] = request.GET.get("from")
        ctx["to"] = request.GET.get("to")
        return render(request, 'site/cargo-details.html', ctx)

    if request.GET.get("service") == "taxi":
        ctx["from"] = request.GET.get("from")
        ctx["to"] = request.GET.get("to")
        return render(request, 'site/taxi-details.html', ctx)

    return render(request, "site/index.html", ctx)

def cargo(request):
    ctx = {}
    return render(request, "site/cargo-details.html", ctx)
