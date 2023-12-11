from django.urls import path
from .views import *

urlpatterns = [
    path('vendors', VendorsView.as_view(), name='vendor-get-post'),
]