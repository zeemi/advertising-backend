from django.contrib import admin

# Register your models here.
from advertising_metrics.models import DataSource, Campaign, Metric


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    pass

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    pass
