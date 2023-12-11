from django.urls import path
from .views import *

urlpatterns = [
    path('vendors', VendorsView.as_view(), name='vendor-view'),
    path('vendors/<int:vendor_id>', VendorsDeatilView.as_view(), name='vendor-detail-view'),
]