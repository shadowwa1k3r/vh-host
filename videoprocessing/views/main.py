from django.views.generic import TemplateView
from videoprocessing.models import Video


class VideoListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(VideoListView, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.all()

        return context
    