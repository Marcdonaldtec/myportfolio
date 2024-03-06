from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .import views

app_name = 'registration'
urlpatterns = [
    path('register', views.register, name='register'),   
    path('login', views.user_login, name='login'),  
    path('logout', views.user_logout, name='logout'),   
    # ... autres URL ...
    path('reset_password/', PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # ... autres URL ...

]


