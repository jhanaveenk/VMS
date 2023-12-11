from rest_framework import serializers
from .models import Vendors


class VendorsSerializer(serializers.Serializer):

    class Meta:
        model = Vendors
        fields = '__all__'