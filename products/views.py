from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductSearchForm
from .models import Product
from . import forms
from django.shortcuts import render, redirect  # make sure redirect is imported
from django.contrib import messages

def add_product(request):
    if request.method == "POST":
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Information added successfully!")
            return redirect('home')  # Make sure 'home' is a named URL in urls.py
    else:
        form = forms.ProductForm()
    return render(request, 'forms.html', {
        "form": form,
    })


def product_search(request):
    if request.method == 'GET':
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            results = Product.objects.filter(blood_group__icontains=search_query)
            return render(request, 'search_results.html', {'results': results})
    else:
        form = ProductSearchForm()
    return render(request, 'home2.html', {'form': form})



def product_search(request):
    if request.method == 'GET':
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            # Filter the products based on blood group
            results = Product.objects.filter(blood_group__icontains=search_query)
            return render(request, 'search.html', {'results': results, 'form': form})
    else:
        form = ProductSearchForm()
    return render(request, 'search.html', {'form': form})


def product_search(request):
    # Get all available donors initially to show all before searching
    products = Product.objects.all()

    if request.method == 'GET':
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            results = Product.objects.filter(blood_group__icontains=search_query)
            return render(request, 'search.html', {'results': results, 'products': products, 'form': form})
    else:
        form = ProductSearchForm()

    return render(request, 'search.html', {'products': products, 'form': form})
from django.shortcuts import redirect





def product_search(request):
    products = Product.objects.all()
    results = products

    if request.method == 'GET':
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            location_query = form.cleaned_data.get('location_query')

            if search_query:
                results = results.filter(blood_group__icontains=search_query)
            if location_query:
                results = results.filter(present_address__icontains=location_query)

            return render(request, 'search.html', {'results': results, 'form': form})
    else:
        form = ProductSearchForm()

    return render(request, 'search.html', {'results': results, 'form': form})

def product_search(request):
    search_query = request.GET.get('search_query', '')
    location_query = request.GET.get('location_query', '')

    results = Product.objects.all()

    if search_query:
        results = results.filter(blood_group__icontains=search_query)
    if location_query:
        results = results.filter(present_address__icontains=location_query)

    context = {
        'products': Product.objects.all(),
        'results': results,
    }
    return render(request, 'home2.html', context)
