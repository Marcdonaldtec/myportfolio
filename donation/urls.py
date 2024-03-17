from django.urls import path
from . import views


app_name='donation'
urlpatterns = [
    path('', views.donation_form, name='donation_form'),
    path('charge/', views.charge, name='charge'),
]
