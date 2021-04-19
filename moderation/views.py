from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.views.generic import ListView

from moderation.forms import CustomUserCreationForm
from moderation.tables import UserTable

# Create your views here.


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('users_table'))
    return render(request, 'registration/register.html', {'form': form})


@login_required
def users_table(request):
    users_table = UserTable(get_user_model().objects.all())
    return render(request, 'moderation/users_table.html', {'table': users_table})


def block_user(pk):
    user = get_user_model().objects.get(pk=pk)
    user.is_active = False
    user.save()


def unblock_user(pk):
    user = get_user_model().objects.get(pk=pk)
    user.is_active = True
    user.save()


def delete_user(pk):
    user = get_user_model().objects.get(pk=pk)
    user.delete()
