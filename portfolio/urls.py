from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns =[
    path('', views.home, name='home' ),
    path('about_me/', views.about_me, name='about_me'),
]

