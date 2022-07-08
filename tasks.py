from __future__ import absolute_import, unicode_literals
import datetime
from celery import shared_task
from Advertisement.models import Click, View
from django.utils import timezone
from Advertisement.models import ClickedCount, ViewedCount
from django.db.models import Sum
from django.db.models import Count
from Advertisement.models import Ad


@shared_task
def clickHourly():
    begin_time = datetime.datetime.now().replace(minute=0, second=0, microsecond=0) - datetime.timedelta(hours=1)
    end_time = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
    selected_clicks = Click.objects.values('Ad_id').annotate(clicked_count=Count('id')).filter(clicked_time__gte=begin_time).filter(clicked_time__lte=end_time)
    count_of_all_ads = selected_clicks.count()
    for i in range(count_of_all_ads):
        instance = ClickedCount()
        instance.count = selected_clicks[i]['clicked_count']
        instance.begin_time = begin_time
        instance.end_time = end_time
        instance.ad = Ad.objects.get(pk=selected_clicks[i]['Ad_id'])
        instance.save()


@shared_task
def viewHourly():
    begin_time = datetime.datetime.now().replace(minute=0, second=0, microsecond=0) - datetime.timedelta(hours=1)
    end_time = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
    selected_view = View.objects.values('Ad_id').annotate(viewed_count=Count('id')).filter(viewed_time__gte=begin_time).filter(viewed_time__lte=end_time)
    count_of_all_ads = selected_view.count()
    for i in range(count_of_all_ads):
        instance = ViewedCount()
        instance.count = selected_view[i]['viewed_count']
        instance.begin_time = begin_time
        instance.end_time = end_time
        instance.ad = Ad.objects.get(pk=selected_view[i]['Ad_id'])
        instance.save()


@shared_task
def clickDaily():
    # TODO : using grou
    now = timezone.now() - datetime.timedelta(days=1)
    return ClickedCount.objects.filter(date__year=now.year,
                                       date__month=now.month,
                                       date__day=now.day,
                                       date__hour=now.hour).aggregate(Sum('count'))


@shared_task
def viewDaily():
    now = timezone.now() - datetime.timedelta(days=1)
    return ViewedCount.objects.filter(date__year=now.year,
                                      date__month=now.month,
                                      date__day=now.day,
                                      date__hour=now.hour).aggregate(Sum('count'))


