from django.contrib import admin

# Register your models here.
from advertising_metrics.models import DataSource, Campaign, Metric


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('date', 'data_source', 'campaign', 'clicks', 'impressions')
