from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Campaign


class CampaignsTests(APITestCase):
    fixtures = ['metrics.json']

    def setUp(self):
        self.CAMPAIGNS_URL = reverse('campaigns')

    def test_listing_data_sources_returns_status_200(self):
        response = self.client.get(self.CAMPAIGNS_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listing_data_sources_returns_all_existing_objects(self):
        response = self.client.get(self.CAMPAIGNS_URL, format='json')
        self.assertEqual(Campaign.objects.count(), len(response.data))

