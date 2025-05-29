from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

from punk_recognizer.models import RecognizeTask
from punk_recognizer.tasks import process_search


class SearchImageView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        image = request.FILES.get('image')
        if not image:
            return Response({'error': 'Image is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Надо подумать че делать с celery_task_id

        rt = RecognizeTask.objects.create(input_image=image)

        task = process_search.delay(rt.pk)

        rt.celery_task_id = task.id
        rt.save()

        return Response({'taskID': task.id}, status=status.HTTP_201_CREATED)
