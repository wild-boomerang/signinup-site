from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse

from moderation.forms import CustomUserCreationForm

# Create your views here.


def dashboard(request):
    return render(request, 'moderation/dashboard.html')


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))
    return render(request, 'registration/register.html', {'form': form})
