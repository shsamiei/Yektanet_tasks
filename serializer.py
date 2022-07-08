from rest_framework import serializers
from Advertisement.models import Ad, Advertiser, View, Click


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        exclude = tuple()


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = tuple()


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ['id', 'ad', 'viewed_time']


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = ['id', 'ad', 'clicked_time']
