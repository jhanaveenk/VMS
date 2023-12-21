from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.db.models import F, Avg
from django.db.models.functions import Coalesce
from django.utils import timezone
from .models import PurchaseOrders, HistoricalPerformaces, Vendors


@receiver(post_save, sender=PurchaseOrders)
def update_vendor_performance_on_save(sender, instance, created, **kwargs):
    vendor = instance.vendor        
    if instance.quality_rating is not None:
        update_quality_rating_avg(vendor)
    if instance.acknowledgment_date:
        update_average_response_time(vendor)
    update_fulfilment_rate(vendor)

@receiver(post_delete, sender=PurchaseOrders)
def update_vendor_performance_on_delete(sender, instance, **kwargs):
    vendor = instance.vendor
    if instance.quality_rating is not None:
        update_quality_rating_avg(vendor)
    update_fulfilment_rate(vendor)

def update_quality_rating_avg(vendor):
    completed_pos = PurchaseOrders.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
    quality_rating_avg = completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg']
    HistoricalPerformaces.objects.update_or_create(vendor=vendor, defaults={'quality_rating_avg': round(quality_rating_avg, 2)})
    Vendors.objects.filter(pk=vendor.pk).update(quality_rating_avg=round(quality_rating_avg, 2))

def update_average_response_time(vendor):
    acknowledged_pos = PurchaseOrders.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    response_times = acknowledged_pos.annotate(
        response_time=Coalesce(F('acknowledgment_date') - F('issue_date'), timezone.timedelta())
    ).aggregate(Avg('response_time'))['response_time__avg']
    HistoricalPerformaces.objects.update_or_create(vendor=vendor, defaults={'average_response_time': response_times})
    Vendors.objects.filter(pk=vendor.pk).update(average_response_time=response_times)

def update_fulfilment_rate(vendor):
    all_pos = PurchaseOrders.objects.filter(vendor=vendor)
    successful_fulfillments = all_pos.filter(status='completed', issue_date__isnull=False, acknowledgment_date__isnull=False)
    fulfilment_rate = round(successful_fulfillments.count() / all_pos.count(), 2) if all_pos.count() > 0 else 0.0
    HistoricalPerformaces.objects.update_or_create(vendor=vendor,  defaults={'fulfillment_rate': fulfilment_rate})
    Vendors.objects.filter(pk=vendor.pk).update(fulfillment_rate=fulfilment_rate)


@receiver(pre_save, sender=PurchaseOrders)
def update_on_time_delivery_rate(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        completed_pos = PurchaseOrders.objects.filter(vendor=vendor, status='completed')
        prev_dilivery_rate = HistoricalPerformaces.objects.get(vendor=vendor).on_time_delivery_rate
        on_time_deliveries = round((completed_pos.count()-1)*prev_dilivery_rate,2)
        if instance.delivery_date >= timezone.now():
            on_time_deliveries = on_time_deliveries+1
        on_time_delivery_rate = round(on_time_deliveries / completed_pos.count(), 2) if completed_pos.count() > 0 else 0.0

        HistoricalPerformaces.objects.filter(vendor=vendor.pk).update(on_time_delivery_rate=on_time_delivery_rate)
        Vendors.objects.filter(pk=vendor.pk).update(on_time_delivery_rate=on_time_delivery_rate)