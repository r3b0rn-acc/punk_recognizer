from django.urls import path, re_path, include
from django.views.generic import TemplateView

from punk_recognizer import views


urlpatterns = [
    path('api/', include([
        path('search/', views.SearchImageView.as_view(), name='image_search'),
        path('status/<str:task_id>/', views.TaskStatusView.as_view(), name='task_status'),
    ])),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
