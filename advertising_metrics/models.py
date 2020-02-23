from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=255, unique=True)


class DataSource(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Metric(models.Model):
    data_sources = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    campaigns = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    clicks = models.BigIntegerField()
    interactions = models.BigIntegerField()
    date = models.DateField()

# todo:
# unique together?
# indexes ?