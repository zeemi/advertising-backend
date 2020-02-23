import io

import requests
from django.conf import settings
from rest_framework import status

from .errors import MetricsError


def get_metrics():
    response = requests.get(settings.METRICS_URL)
    if response.status_code != status.HTTP_200_OK:
        raise MetricsError('Cannot fetch metrics: error {}'.format(response.status_code))
    return io.StringIO(response.text)
