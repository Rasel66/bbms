from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm, DonorForm


def homePage(request):
    return render(request, 'homePage.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def whyDonateBloodPage(request):
    return render(request, 'whyDonateBlood.html')

def donor_views(request):
    form = DonorForm()
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
        
            messages.success(request, "Information is saved successfully!!!")
            return redirect('homePage')
        else:
            print(form.errors)
    context={
        'form': form
    }
    return render(request, 'donor.html', context)


