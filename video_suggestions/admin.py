from django.contrib import admin
from .models import Reason, FakeVideo, VideoHasReasons

# Register your models here.

admin.site.register(Reason)
admin.site.register(FakeVideo)
admin.site.register(VideoHasReasons)
