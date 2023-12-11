from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VendorsSerializer, PurchaseOrdersSerializer
from .models import Vendors, PurchaseOrders


class VendorsView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Vendors.objects.all().order_by('id')
        serializer = VendorsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = VendorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class VendorsDeatilView(APIView):

    def get(self, request, *args, **kwargs):
        vendor_id = kwargs["vendor_id"]
        try:
            queryset = Vendors.objects.get(id=vendor_id)
        except Vendors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VendorsSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        vendor_id = kwargs["vendor_id"]
        try:
            queryset = Vendors.objects.get(id=vendor_id)
        except Vendors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VendorsSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        vendor_id = kwargs["vendor_id"]
        try:
            queryset = Vendors.objects.get(id=vendor_id)
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vendors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PurchaseOrdersView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = PurchaseOrders.objects.all()
        serializer = PurchaseOrdersSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)