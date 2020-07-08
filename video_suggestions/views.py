from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Reason, FakeVideo
from .forms import ReasonForm

# Create your views here.

class VideoSuggestionView(View):
    def get(self, request, *args, **kwargs):
        fakeVideo = get_object_or_404(FakeVideo, id=kwargs['id'])
        form = ReasonForm()
        context = {
            'fakeVideo': fakeVideo,
            'form': form
        }
        return render(request=request, template_name='video_suggestions/suggest_reasons.html', context=context)

    def post(self, request, *args, **kwargs):
        fakeVideo = get_object_or_404(FakeVideo, id=kwargs['id'])
        form = ReasonForm(request.POST)
        if form.is_valid():
            reason = form.save()
            fakeVideo.reasons.add(reason)
        context = {}
        return render(request=request, template_name='video_suggestions/thank_you.html', context=context)
