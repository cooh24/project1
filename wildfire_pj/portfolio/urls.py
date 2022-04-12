from django.urls import path
from . import views

urlpatterns = [
    path('port1/', views.port1),
    path('port2/', views.port2),
    path('port3/', views.port3),
    path('port4/', views.port4),

]