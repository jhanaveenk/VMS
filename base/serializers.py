from django.utils import timezone
from rest_framework import serializers
from .models import Vendors, PurchaseOrders, HistoricalPerformaces


class VendorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendors
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):

    # def validate(self, data):
    #     print("validated_data:", self.validated_data)
    #     print("initial_data:", self.initial_data)
    # # Your validation logic here
    #     return data

    def validate_quality_rating(self, value):
        if not 0 <= value <= 5:
            raise serializers.ValidationError("Quality rating should be between 0 and 5.")
        return value

    def validate_issue_date(self, value):
        print(value)
        instance = self.instance
        if instance and instance.vendor:
            # Set issue_date to the current time if vendor is present
            value = timezone.now()

        return value

    # def validate_quantity(self, data):
    #     if 'items' in data and data['items'] is not None:
    #         quantity = 0
    #         for item in data["items"]:
    #             quantity += item.get("quantity")
    #         if data.get("quantity") is None or data.get("quantity") != quantity:
    #             data["quantity"] = quantity
    #     return data
    class Meta:
        model = PurchaseOrders
        fields = '__all__'
    
class VendorPerfomanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricalPerformaces
        fields = '__all__'