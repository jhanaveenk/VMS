from django.utils import timezone
from rest_framework import serializers
from .models import Vendors, PurchaseOrders, HistoricalPerformaces


class VendorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendors
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):

    def validate_quality_rating(self, value):
        if not 0 <= value <= 5:
            print('hello')
            raise serializers.ValidationError("Quality rating should be between 0 and 5.")
        return value
    
    def validate(self, data):
        if 'vendor' in data:
            data["issue_date"] = timezone.now()
        if 'items' in data:
            quantity=0
            for item in data["items"]:
                quantity += item.get("quantity")
            if data.get("quantity") is None or data.get("quantity") != quantity:
                 data["quantity"] = quantity
        return data

    class Meta:
        model = PurchaseOrders
        fields = '__all__'
    
class VendorPerfomanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricalPerformaces
        fields = '__all__'