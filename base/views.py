from django.db import models
from rest_framework import status
from django.utils import timezone
from django.db.models import F, Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vendors, PurchaseOrders, HistoricalPerformaces
from .serializers import VendorsSerializer, PurchaseOrderSerializer, VendorPerfomanceSerializer


class VendorsView(APIView):

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

    def get(self, request, *args, **kwargs):
        po_id = kwargs["po_id"]
        try:
            purchase_instance = PurchaseOrders.objects.get(id=po_id)
        except PurchaseOrders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        purchase_instance.acknowledgment_date = timezone.now()
        purchase_instance.save()
        return Response("Order acknowledged sucessfully", status=status.HTTP_202_ACCEPTED)

"""
On-Time Delivery Rate:
● Calculated each time a PO status changes to 'completed'.
● Logic: Count the number of completed POs delivered on or before
delivery_date and divide by the total number of completed POs for that vendor.
"""


class VendorPerfomance(APIView):

    def on_time_delivery_rate(self, vendor_id):
        pass

    def average_rating_calculation(self, vendor_id):
        quality_rating_avg = PurchaseOrders.objects.filter(vendor_id=vendor_id, status='completed', quality_rating__isnull=False).aggregate(average_rating=Avg('quality_rating'))
        if quality_rating_avg.get("average_rating") is None:
            return 0
        return quality_rating_avg.get("average_rating", 0.00)
        
    def fulfillment_rate_calculation(self, vendor_id):
        fulfillment_rate_queryset = PurchaseOrders.objects.filter(vendor_id=vendor_id)
        total_count , fulfilled_count = len(fulfillment_rate_queryset), 0
        for obj in fulfillment_rate_queryset:
            if obj.status == 'completed':
                fulfilled_count += 1
        if total_count == 0:
            fulfilled_orders = 0.00
        else:
            fulfilled_orders = fulfilled_count/total_count
        return fulfilled_orders

    def average_response_time_calculation(self, vendor_id):
        average_response_time_queryset = PurchaseOrders.objects.filter(vendor_id=vendor_id, acknowledgment_date__isnull=False).aggregate(
        avg_time=Avg(F('acknowledgment_date') - F('issue_date'),output_field=models.DurationField()))
        return average_response_time_queryset.get("avg_time")

    def get(self, request, *args, **kwargs):
        vendor_id = kwargs["vendor_id"]
        try:
            performance_instance = HistoricalPerformaces.objects.get(vendor_id=vendor_id)
        except HistoricalPerformaces.DoesNotExist:
            performance_instance = HistoricalPerformaces.objects.create(vendor_id=vendor_id)
        
        performance_instance.quality_rating_avg = round(self.average_rating_calculation(vendor_id), 2)
        performance_instance.fulfillment_rate = round(self.fulfillment_rate_calculation(vendor_id), 2)
        performance_instance.average_response_time = self.average_response_time_calculation(vendor_id)
        performance_instance.save()
        performance_serializer = VendorPerfomanceSerializer(performance_instance)
        return Response(performance_serializer.data)