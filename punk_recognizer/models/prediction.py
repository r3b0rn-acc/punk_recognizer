from django.conf import settings

from django.contrib import admin
from django.db import models


class Prediction(models.Model):
    input_image = models.ImageField(upload_to='input_images/')

    photo_path = models.FilePathField(path=settings.BASE_DIR / 'classifier' / 'dataset', recursive=True)
    label = models.CharField(max_length=32)

    task = models.ForeignKey('punk_recognizer.RecognizeTask', on_delete=models.PROTECT)

    class Admin(admin.ModelAdmin):
        list_display = ('photo_path', 'label', 'task')
        list_filter = ('task', 'label')
        search_fields = ('photo_path', 'label')
