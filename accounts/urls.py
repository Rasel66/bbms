from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name='homePage'),
    path('register/', register_view, name='register'),
    path('why-donate-blood/', whyDonateBloodPage, name='why_donate_blood_page'),
    path('become-donor/', donor_views, name='donor'),
]


