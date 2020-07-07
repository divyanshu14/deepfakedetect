from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Reason, FakeVideo

# Create your views here.

class VideoSuggestionView(View):
    def get(self, request, *args, **kwargs):
        reasons = Reason.objects.all()
        fakeVideo = get_object_or_404(FakeVideo, id=kwargs['id'])
        context = {
            'reasons': reasons,
            'fakeVideo': fakeVideo
        }
        return render(request=request, template_name='video_suggestions/suggest_reasons.html', context=context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request=request, template_name='video_suggestions/thank_you.html', context=context)
