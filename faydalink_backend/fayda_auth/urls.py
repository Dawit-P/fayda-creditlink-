from django.urls import path
from .views import FaydaLogin, CustomerSearch

urlpatterns = [
    path('login/', FaydaLogin.as_view(), name='fayda-login'),
    path('search/', CustomerSearch.as_view(), name='customer-search'),
]
