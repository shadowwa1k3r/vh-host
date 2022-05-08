from rest_framework.response import Response
from rest_framework.views import APIView

from videoprocessing.models import Video
from .serializers import VideoSerializer
from videoprocessing.tasks import create_task
import boto3


class VideoUploadAPIView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        print(request.FILES)
        print(request.POST)
        vid = Video.objects.create()
        session = boto3.Session(
            aws_access_key_id='AKIAZVZNJBXI35X2S4MP',
            aws_secret_access_key='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'
        )
        s3 = session.resource('s3')
        result = s3.Bucket('vh-s3').put_object(Body=file, Key='{}/{}'.format(str(vid.id), file.name))
        task = create_task.delay(vid.id, file.name)
        return Response(status=200)


class VideoProcessUpdateAPIView(APIView):
    def patch(self, request, video_id):
        vid = Video.objects.get(id=video_id)
        serializer = VideoSerializer(vid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=204)
        return Response(status=400)

