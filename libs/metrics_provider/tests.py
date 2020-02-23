import unittest
from collections import Iterable

import requests_mock
from django.conf import settings

from libs.metrics_provider.errors import MetricsError
from . import get_metrics

csv_text = '''Date,Datasource,Campaign,Clicks,Impressions
30.06.2019,Google Adwords,Summer Offer 2019 - Prio 1,31,502
30.06.2019,Google Adwords,Summer Offer 2019 - Prio 2,14,480
30.06.2019,Google Adwords,Summer Offer 2019 - Prio 3,44,1029
30.06.2019,Google Adwords,Summer Offer 2019 - Prio 4,65,1148
30.06.2019,Google Analytics,GDN Prospecting - Prio 1 Offer,91,25578
30.06.2019,Google Analytics,GDN Prospecting - Prio 2 Offer,131,44641
30.06.2019,Google Analytics,GDN RMKT - India Offer,162,23043
30.06.2019,Google Analytics,GDN RMKT - Prio 1 Offer,28,11271
30.06.2019,Google Analytics,GDN RMKT - Prio 2 Offer,116,27640
30.06.2019,Google Analytics,Summer Offer 2019 - India,48,924
30.06.2019,Google Analytics,Summer Offer 2019 - Prio 1,31,502
30.06.2019,Google Analytics,Summer Offer 2019 - Prio 2,14,480
30.06.2019,Google Analytics,Summer Offer 2019 - Prio 3,44,1029
30.06.2019,Google Analytics,Summer Offer 2019 - Prio 4,65,1148
30.06.2019,Mailchimp,Summer Offer 2019 | Extension,852, 15
'''


@requests_mock.mock()
class TestMetricsProvider(unittest.TestCase):

    def test_get_metrics_calls_external_api(self, request_mock_adapter):
        request_mock_adapter.register_uri(
            'GET',
            settings.METRICS_URL, text='{"Response": true}'
        )
        get_metrics()
        self.assertEqual(request_mock_adapter.call_count, 1)

    def test_get_metrics_returns_iterable(self, request_mock_adapter):
        request_mock_adapter.register_uri(
            'GET',
            settings.METRICS_URL, text=csv_text
        )
        self.assertTrue(isinstance(get_metrics(), Iterable))

    def test_get_metrics_raise_MetricsError_on_failure(self, request_mock_adapter):
        request_mock_adapter.register_uri(
            'GET',
            settings.METRICS_URL, text='{"Response": true}', status_code=400
        )
        self.assertRaises(MetricsError, get_metrics)

