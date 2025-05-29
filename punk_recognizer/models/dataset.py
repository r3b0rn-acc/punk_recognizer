import os

import pandas as pd

from django.contrib import admin
from django.db import models

from punk_recognizer.storages import DatasetStorage


class Dataset(models.Model):
    dataset = models.FileField(upload_to='', storage=DatasetStorage(), blank=True, null=True)

    batch_size = models.IntegerField(default=32)
    img_axis_size = models.IntegerField(default=512)
    num_classes = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def collect_data(cls, data_path: str, output_path: str):
        if not os.path.exists(data_path):
            raise Exception('Dataset directory does not exist')

        df = pd.DataFrame(columns=('path', 'label'))

        for dir_name in os.listdir(data_path):
            dir_path = os.path.join(data_path, dir_name)
            if not os.path.isdir(dir_path):
                continue
            for file_name in os.listdir(dir_path):
                df.loc[len(df)] = (os.path.join(dir_path, file_name), dir_name)

        output_csv_path = os.path.join(output_path, 'dataset.csv')
        df.to_csv(output_csv_path, index=False)

        return cls.objects.get_or_create(dataset=output_csv_path)

    class Admin(admin.ModelAdmin):
        list_display = ('dataset', 'created_at', 'updated_at')
        list_display_links = ('dataset',)
