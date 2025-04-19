from .views import loginView
from django.urls import path

urlpatterns = [
    path('login',loginView,name='login')
]