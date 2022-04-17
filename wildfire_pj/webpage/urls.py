from django.urls import path
from . import views

urlpatterns = [
    path('web1/', views.web1),
    path('web2/', views.web2),
    path('web3/', views.web3),
]