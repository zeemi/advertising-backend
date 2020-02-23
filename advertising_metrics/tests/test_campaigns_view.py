from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import DataSource


class DataSourcesTests(APITestCase):
    fixtures = ['metrics.json']

    def setUp(self):
        self.DATA_SOURCES_URL = reverse('data_sources')

    def test_listing_data_sources_returns_status_200(self):
        response = self.client.get(self.DATA_SOURCES_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listing_data_sources_returns_all_existing_objects(self):
        response = self.client.get(self.DATA_SOURCES_URL, format='json')
        self.assertEqual(DataSource.objects.count(), len(response.data))

