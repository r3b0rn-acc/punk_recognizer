import os

from celery import shared_task

from django.conf import settings
from django.utils import timezone

from punk_recognizer.models import Prediction, RecognizeTask


os.environ["CUDA_VISIBLE_DEVICES"] = ""


_searcher_instance = None


# А-ля кэш, т.к. Tensorflow не любит инициализацию до fork
def get_searcher():
    global _searcher_instance
    if _searcher_instance is None:
        from classifier.classes.image_searcher import ImageSearcher
        base = settings.BASE_DIR / 'classifier'
        _searcher_instance = ImageSearcher(
            dataset_path=base / 'dataset' / 'dataset.csv',
            index_path=base / 'indexes' / 'index.pkl',
            weights_path=base / 'weights' / 'best_classifier.weights.h5',
        )
    return _searcher_instance


@shared_task
def process_search(recognize_task_pk: int):
    recognize_task = RecognizeTask.objects.get(pk=recognize_task_pk)

    try:
        searcher = get_searcher()

        result = searcher.search(recognize_task.input_image.path)

    except Exception as e:
        print(f"Error in task {recognize_task_pk}: {e}")
        recognize_task.finished_at = timezone.now()
        recognize_task.save()
        raise

    recognize_task.finished_at = timezone.now()
    recognize_task.save()

    predictions = [
        Prediction(photo_path=p.get('image_path'), label=p.get('label'), dist=p.get('dist'), task=recognize_task)
        for p in result
    ]
    Prediction.objects.bulk_create(predictions)

    return result
