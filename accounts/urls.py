from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name='homePage'),
    path('register/', register_view, name='register'),
]


