from rest_framework import serializers

from .models import DataSource, Campaign, Metric


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        exclude = []


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        exclude = []


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        exclude = ('id', )
