from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", views.register, name='register'),
    url(r"^", views.users_table, name='users_table'),
]
