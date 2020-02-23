
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import DataSource
from .serializers import DataSourceSerializer


class DataSourceView(generics.ListAPIView):
    """
    A simple View for listing data sources.
    """

    serializer_class = DataSourceSerializer
    permission_classes = (AllowAny,)
    queryset = DataSource.objects.all()
    pagination_class = None

