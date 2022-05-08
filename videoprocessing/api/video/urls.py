from django.urls import path
from .views import VideoUploadAPIView, VideoProcessUpdateAPIView

urlpatterns = [
    path('upload/', VideoUploadAPIView.as_view(), name='video-upload'),
    path('update/<int:video_id>/', VideoProcessUpdateAPIView.as_view(), name='video-update'),
]