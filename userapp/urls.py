from django.urls import path, include
from . import views

urlpatterns = [
    path('form/', views.form, name='form'),
    path('login/', views.login, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('email/', views.email, name='email')

]


