from rest_framework import status
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VendorsSerializer, PurchaseOrderSerializer, VendorPerfomanceSerializer
from .models import Vendors, PurchaseOrders, HistoricalPerformaces


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
        purchase_queryset = PurchaseOrders.objects.all()
        po_serializer = PurchaseOrderSerializer(purchase_queryset, many=True)
        return Response(po_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        po_serializer = PurchaseOrderSerializer(data=request.data)
        print(po_serializer)
        if po_serializer.is_valid():
            po_serializer.save()
            return Response(po_serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
"""
Payload:
{
    "po_number": "ucebva6aceuaijk",
    "vendor": 8,
    "items": [
        {"name": "Item1", "quantity": 10},
        {"name": "Item2", "quantity": 5}
    ],
    "quantity": 15,
    "status": "pending"
}
"""
    
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
    
    """
    PAYLOAD
    {
    "delivery_date" : "2023-12-15T08:00:10.000000Z",
    "status":"completed"
    }
    """

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



class VendorPerfomance(APIView):
    def get(self, request, *args, **kwargs):
        vendor_id = kwargs["vendor_id"]
        try:
            performance_instance = HistoricalPerformaces.objects.get_or_create(vendor_id=vendor_id)
        except:
            return Response("No Vendor at given ID")
        performance_serializer = VendorPerfomanceSerializer(performance_instance)

        return Response(performance_serializer)