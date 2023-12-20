import uuid
from django.db import models

class Vendors(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    vendor_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class PurchaseOrders(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    po_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    vendor = models.ForeignKey('base.Vendors', on_delete=models.CASCADE, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True) 
    items = models.JSONField()
    quantity = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True , blank=True)
    issue_date = models.DateTimeField(null=True, blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    

class HistoricalPerformaces(models.Model):
    vendor = models.ForeignKey('base.Vendors', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.DurationField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)