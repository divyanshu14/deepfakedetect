from django.db import models

# Create your models here.

class Reason(models.Model):
    reasonText = models.TextField()

class FakeVideo(models.Model):
    title = models.CharField(max_length=64)
    video = models.FileField(upload_to='deep-fake-videos')

class VideoHasReasons(models.Model):
    fake_video = models.ForeignKey(to=FakeVideo, on_delete=models.CASCADE)
    reason = models.ForeignKey(to=Reason, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fake_video', 'reason'], name='unique_reason_for_video')
        ]
