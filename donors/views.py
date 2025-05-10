from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse  # To dynamically get the URL for redirection
from . import forms


def add_donor(request):
    if request.method == "POST":  # Use POST for form submission
        form = forms.DonorForm(request.POST)  # Handle POST data
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))  # Redirect to the home page
    else:
        form = forms.DonorForm()  # Instantiate an empty form for GET requests

    return render(request, 'formsnew.html', {
        "form": form,
    })




from django.shortcuts import render
from .models import Donor

def donor_list(request):
    blood_group = request.GET.get('blood_group')
    when_needed = request.GET.get('when_needed')

    donors = Donor.objects.all()

    if blood_group:
        donors = donors.filter(blood_group=blood_group)

    if when_needed:
        donors = donors.filter(when_needed__date=when_needed)  # compare only date part

    return render(request, 'home3.html', {
        'donors': donors,
    })


from django.shortcuts import render
from .models import Donor

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'home3.html', {'donors': donors})

def filtered_donors(request):
    donors = Donor.objects.all()

    blood_group = request.GET.get('blood_group')
    when_needed = request.GET.get('when_needed')

    if blood_group:
        donors = donors.filter(blood_group=blood_group)

    if when_needed:
        donors = donors.filter(when_needed__date=when_needed)

    return render(request, 'filtered_donors.html', {
        'donors': donors,
    })




