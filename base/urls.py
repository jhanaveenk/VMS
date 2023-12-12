from django.urls import path
from .views import *

urlpatterns = [
    path('vendors', VendorsView.as_view(), name='vendor-view'),
    path('vendors/<int:vendor_id>', VendorsDeatilView.as_view(), name='vendor-detail-view'),
    path('purchase_orders', PurchaseOrdersView.as_view(), name='purchase-orders'),
    path('purchase_orders/<int:po_id>', PurchaseOrdersDetailView.as_view(), name='purchase-detail-view'),
    path('purchase_orders/<int:po_id>/acknowledge', OrderAcknowledgeView.as_view(), name='order-acknowledge')
]