from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Metric


class MetricsTests(APITestCase):
    fixtures = ['metrics.json']

    def setUp(self):
        self.METRICS_URL = reverse('metrics')

    def test_listing_metrics_returns_status_200(self):
        response = self.client.get(self.METRICS_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listing_metrics_returns_all_existing_objects(self):
        response = self.client.get(self.METRICS_URL, format='json')
        self.assertEqual(Metric.objects.count(), len(response.data))

