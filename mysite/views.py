from django.shortcuts import render
from products.models import Product
from donors.models import Donor


def home(request):
    products = Product.objects.all()
    donors = Donor.objects.all()
    return render(request, 'home.html', {
        "products": products,
        "donors": donors,
    })


def another(request):
    products = Product.objects.all()
    return render(request, 'home1.html')


def another_new(request):
    products = Product.objects.all()
    donors = Donor.objects.all()
    return render(request, 'home2.html', {
        "products": products,
        "donors": donors,
    })


def another_second(request):
    products = Product.objects.all()
    donors = Donor.objects.all()
    return render(request, 'home3.html', {
        "products": products,
        "donors": donors,
    })
