from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.OrdersValidationView.as_view(), name='orders'),
]