from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class DataSource(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Metric(models.Model):
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    clicks = models.BigIntegerField(default=0)
    impressions = models.BigIntegerField(default=0)
    date = models.DateField()

# todo:
# unique together?
# indexes ?