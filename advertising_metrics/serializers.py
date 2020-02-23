from rest_framework import serializers

from .models import DataSource, Campaign


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        exclude = []


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        exclude = []
