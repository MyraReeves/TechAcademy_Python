from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('create_new_account/', views.create_account, name='create'),
    path('<int:pk>/balance_sheet/', views.balance, name='balance'),
    path('add_new_transaction/', views.transaction, name='transaction'),
]