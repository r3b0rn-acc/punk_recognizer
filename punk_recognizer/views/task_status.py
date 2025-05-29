from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from celery.result import AsyncResult

from punk_recognizer.models import RecognizeTask


class TaskStatusView(APIView):
    def get(self, request, task_id):
        try:
            task = RecognizeTask.objects.get(celery_task_id=task_id)
        except RecognizeTask.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        result = AsyncResult(task_id)

        position = RecognizeTask.objects.filter(
            finished_at__isnull=True,
            created_at__lt=task.created_at
        ).count() + 1

        if result.ready():
            position = 0

        return Response({
            'task_id': task_id,
            'status': result.status,
            'result': result.result if result.ready() else None,
            'position': position,
        })
