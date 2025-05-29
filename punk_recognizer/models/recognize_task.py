from django.contrib import admin
from django.db import models


class RecognizeTask(models.Model):
    celery_task_id = models.CharField(max_length=64, blank=True, null=True)  # Костыль с blank и null

    input_image = models.ImageField(upload_to='input_images/')

    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    class Admin(admin.ModelAdmin):
        list_display = ('created_at', 'finished_at')
        list_filter = ('created_at', 'finished_at')
        search_fields = ('created_at', 'finished_at')
        date_hierarchy = 'created_at'
