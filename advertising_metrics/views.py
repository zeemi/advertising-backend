from django.db.models import Sum
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import DataSource, Campaign, Metric
from .serializers import DataSourceSerializer, CampaignSerializer, MetricSerializer


class DataSourcesView(generics.ListAPIView):
    """
    A simple View for listing data sources.
    """

    serializer_class = DataSourceSerializer
    permission_classes = (AllowAny,)
    queryset = DataSource.objects.all()
    pagination_class = None


class CampaignsView(generics.ListAPIView):
    """
    A simple View for listing campaigns.
    """

    serializer_class = CampaignSerializer
    permission_classes = (AllowAny,)
    queryset = Campaign.objects.all()
    pagination_class = None


class MetricsView(generics.ListAPIView):
    """
    A simple View for listing and filtering metrics.
    """

    serializer_class = MetricSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    def get_queryset(self):
        params = {}
        if 'campaigns' in self.request.GET and self.request.GET['campaigns']:
            params['campaign__in'] = self.request.GET['campaigns'].split(',')

        if 'data-sources' in self.request.GET and self.request.GET['data-sources']:
            params['data_source__in'] = self.request.GET['data-sources'].split(',')

        return Metric.objects.filter(**params).values('date') \
            .annotate(clicks=Sum('clicks')) \
            .annotate(impressions=Sum('impressions'))
