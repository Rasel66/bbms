from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

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


