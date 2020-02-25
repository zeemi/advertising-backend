from django.db.models import Sum
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

    def test_listing_metrics_returns_summary_of_all_metrics(self):
        response = self.client.get(self.METRICS_URL, format='json')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['date'], '2019-06-30')
        self.assertEqual(Metric.objects.aggregate(Sum('clicks'))['clicks__sum'], response.data[0]['clicks'])
        self.assertEqual(Metric.objects.aggregate(Sum('impressions'))['impressions__sum'],
                         response.data[0]['impressions'])

    def test_listing_metrics_is_filtered_by_campaigns(self):
        response = self.client.get('{}?campaigns=8,11'.format(self.METRICS_URL))
        self.assertEqual(Metric.objects.filter(campaign__in=[8, 11]).aggregate(Sum('clicks'))['clicks__sum'],
                         response.data[0]['clicks'])
        self.assertEqual(Metric.objects.filter(campaign__in=[8, 11]).aggregate(Sum('impressions'))['impressions__sum'],
                         response.data[0]['impressions'])

    def test_listing_metrics_is_filtered_by_data_source(self):
        response = self.client.get('{}?data-sources=1'.format(self.METRICS_URL))
        self.assertEqual(Metric.objects.filter(data_source__in=[1]).aggregate(Sum('clicks'))['clicks__sum'],
                         response.data[0]['clicks'])
        self.assertEqual(Metric.objects.filter(data_source__in=[1]).aggregate(Sum('impressions'))['impressions__sum'],
                         response.data[0]['impressions'])

    def test_listing_metrics_is_filtered_by_campaigns_and_data_sources(self):
        response = self.client.get('{}?campaigns=3,4&data-sources=1,2'.format(self.METRICS_URL))
        self.assertEqual(
            Metric.objects.filter(data_source__in=[1, 2], campaign__in=[3, 4]).aggregate(Sum('clicks'))['clicks__sum'],
            response.data[0]['clicks'])
        self.assertEqual(
            Metric.objects.filter(data_source__in=[1, 2], campaign__in=[3, 4]).aggregate(Sum('impressions'))[
                'impressions__sum'], response.data[0]['impressions'])
