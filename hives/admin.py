from django.contrib import admin
from .models import *


@admin.register(Hive)
class HiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'coordinate',)


@admin.register(DataHive)
class DataHiveAdmin(admin.ModelAdmin):
    list_display = ('hive_id', 'date', 'temperature', 'humidity', 'weight')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'hive_id', 'service', 'coast')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_of_request')


@admin.register(ReportHive)
class ReportHiveAdmin(admin.ModelAdmin):
    list_display = ('hive_id', 'aver_temp', 'aver_humid', 'change_weight', 'end_date')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('number', 'valid', 'cvv')
