from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('users', views.username_list, name="users"),

    # path(full url path, call the "details" method from views file, nickname of this path)
    path('<int:pk>/details/', views.details, name="details"),
]