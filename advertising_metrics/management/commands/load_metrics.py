import csv
import io
from logging import getLogger
from datetime import datetime

from django.core.management.base import BaseCommand

from ...models import Campaign, Metric, DataSource

logger = getLogger(__name__)

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


def fetch_data():
    return io.StringIO(csv_text)


class Command(BaseCommand):
    help = 'This command fetches metrics and populate local databases with downloaded data'

    def handle(self, *args, **options):
        logger.info('Loading started ...')
        reader = csv.DictReader(fetch_data())
        logger.info('Data prepared.')

        for row in reader:
            campaign, is_created = Campaign.objects.update_or_create(name=row['Campaign'])
            data_source, is_created = DataSource.objects.update_or_create(name=row['Datasource'])
            Metric.objects.update_or_create(campaign=campaign, data_source=data_source,
                                            date=datetime.strptime(row['Date'], '%d.%m.%Y'),
                                            defaults={'clicks': row['Clicks'] or 0,
                                                      'impressions': row['Impressions'] or 0})


        logger.info('Data processed.')
