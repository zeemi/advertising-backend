import csv
import io
from logging import getLogger
from datetime import datetime

from django.core.management.base import BaseCommand

from ...models import Campaign, Metric, DataSource

from libs.metrics_provider import get_metrics

logger = getLogger(__name__)


class Command(BaseCommand):
    help = 'This command fetches metrics and populate local databases with downloaded data'

    def handle(self, *args, **options):
        logger.info('Loading started ...')
        reader = csv.DictReader(get_metrics())
        logger.info('Data prepared.')
        for row in reader:
            campaign, is_created = Campaign.objects.update_or_create(name=row['Campaign'])
            data_source, is_created = DataSource.objects.update_or_create(name=row['Datasource'])
            Metric.objects.update_or_create(campaign=campaign, data_source=data_source,
                                            date=datetime.strptime(row['Date'], '%d.%m.%Y'),
                                            defaults={'clicks': row['Clicks'] or 0,
                                                      'impressions': row['Impressions'] or 0})


        logger.info('Data processed.')
