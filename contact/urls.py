from django.urls import path
from .views import home,contact_list,contact_details
urlpatterns = [
    path('',home,name='index'),
    path('contact',contact_list,name='contact'),
    path('contact/<int:id>',contact_details,name='details')
]