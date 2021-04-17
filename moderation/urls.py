from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r"^dashboard/", views.dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", views.register, name='register'),
    # path('', views.index, name='index'),
    # path('reports/', views.reports, name='reports'),
]