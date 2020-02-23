
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import DataSource, Campaign
from .serializers import DataSourceSerializer, CampaignSerializer


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

