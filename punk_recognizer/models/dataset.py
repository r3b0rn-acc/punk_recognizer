from django.contrib import admin
from django.db import models

from punk_recognizer.storages import DatasetStorage


class Dataset(models.Model):
    dataset = models.FileField(upload_to='', storage=DatasetStorage(), blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Admin(admin.ModelAdmin):
        list_display = ('dataset', 'created_at', 'updated_at')
        list_display_links = ('dataset',)
