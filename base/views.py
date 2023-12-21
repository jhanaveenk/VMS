from django.db import models
from rest_framework import status
from django.utils import timezone
from django.db.models import F, Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vendors, PurchaseOrders, HistoricalPerformaces
from .serializers import VendorsSerializer, PurchaseOrderSerializer, VendorPerfomanceSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated


class VendorsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        vendor_queryset = Vendors.objects.all().order_by('id')
        ven_serializer = VendorsSerializer(vendor_queryset, many=True)
        return Response(ven_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        ven_serializer = VendorsSerializer(data=request.data)
        if ven_serializer.is_valid():
            ven_serializer.save()
            return Response(ven_serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class VendorsDeatilView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        vendor_id = kwargs["vendor_id"]
        try:
            vendor_instance = Vendors.objects.get(id=vendor_id)
        except Vendors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ven_serializer = VendorsSerializer(vendor_instance)
        return Response(ven_serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        vendor_id = kwargs["vendor_id"]
        try:
            vendor_instance = Vendors.objects.get(id=vendor_id)
        except Vendors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ven_serializer = VendorsSerializer(vendor_instance, data=request.data, partial=True)
        if ven_serializer.is_valid():
            ven_serializer.save()
            return Response(ven_serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        vendor_id = kwargs["vendor_id"]
        try:
            vendor_instance = Vendors.objects.get(id=vendor_id)
            vendor_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vendors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PurchaseOrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        purchase_queryset = PurchaseOrders.objects.all().order_by('id')
        po_serializer = PurchaseOrderSerializer(purchase_queryset, many=True)
        return Response(po_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        po_serializer = PurchaseOrderSerializer(data=request.data)
        if po_serializer.is_valid():
            po_serializer.save()
            return Response(po_serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
class PurchaseOrdersDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        po_id = kwargs["po_id"]
        try:
            purchase_instance = PurchaseOrders.objects.get(id=po_id)
        except PurchaseOrders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        po_serializer = PurchaseOrderSerializer(purchase_instance)
        return Response(po_serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        po_id = kwargs["po_id"]
        try:
            purchase_instance = PurchaseOrders.objects.get(id=po_id)
        except PurchaseOrders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        po_serializer = PurchaseOrderSerializer(purchase_instance, data=request.data, partial=True)
        if po_serializer.is_valid():
            po_serializer.save()
            return Response(po_serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        po_id = kwargs["po_id"]
        try:
            purchase_instance = PurchaseOrders.objects.get(id=po_id)
            purchase_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PurchaseOrders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class OrderAcknowledgeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        po_id = kwargs["po_id"]
        try:
            purchase_instance = PurchaseOrders.objects.get(id=po_id)
        except PurchaseOrders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        purchase_instance.acknowledgment_date = timezone.now()
        purchase_instance.save()
        return Response("Order acknowledged sucessfully", status=status.HTTP_202_ACCEPTED)

class VendorPerfomance(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        vendor_id = kwargs["vendor_id"]
        try:
            performance_instance = HistoricalPerformaces.objects.get(vendor_id=vendor_id)
        except HistoricalPerformaces.DoesNotExist:
            return Response('Data for this vendor does not exists', status=status.HTTP_404_NOT_FOUND)
        performance_serializer = VendorPerfomanceSerializer(performance_instance)
        return Response(performance_serializer.data)