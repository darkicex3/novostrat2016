from django.shortcuts import render
from django.http import HttpResponse


def products(request):
    return render(request, 'products/products.html')


def automotive(request):
    return HttpResponse("Automotive")


def insulation(request):
    return HttpResponse("Insulation")


def packaging(request):
    return HttpResponse("Packaging")




