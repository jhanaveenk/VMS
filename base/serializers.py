from rest_framework import serializers
from .models import Vendors, PurchaseOrders


class VendorsSerializer(serializers.ModelSerializer):
# when vendor created their unique 7 char code should created automatically
    class Meta:
        model = Vendors
        fields = '__all__'

class PurchaseOrdersSerializer(serializers.ModelSerializer):
## figure out all fields
    class Meta:
        model = PurchaseOrders
        fields = '__all__'