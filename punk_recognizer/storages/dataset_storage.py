from django.conf import settings

from django.core.files.storage import FileSystemStorage


class DatasetStorage(FileSystemStorage):
    def __init__(self, location=settings.BASE_DIR / 'classifier' / 'dataset'):
        super().__init__(location)

    def url(self, name):
        raise NotImplementedError('URL access is disabled for dataset storage')
