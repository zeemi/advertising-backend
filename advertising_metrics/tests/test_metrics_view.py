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

    def test_listing_metrics_is_filtered_by_campaigns(self):
        response = self.client.get('{}?campaigns=8,11'.format(self.METRICS_URL))
        self.assertEqual(Metric.objects.filter(campaign__in=[8, 11]).count(), len(response.data))

    def test_listing_metrics_is_filtered_by_data_source(self):
        response = self.client.get('{}?data-sources=1'.format(self.METRICS_URL))
        self.assertEqual(Metric.objects.filter(data_source__in=[1]).count(), len(response.data))

    def test_listing_metrics_is_filtered_by_campaigns_and_data_sources(self):
        response = self.client.get('{}?campaigns=1,2&data-sources=3,4'.format(self.METRICS_URL))
        self.assertEqual(Metric.objects.filter(campaign__in=[1, 2], data_source__in=[3, 4]).count(), len(response.data))
