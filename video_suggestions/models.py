from django.db import models

# Create your models here.

class Reason(models.Model):
    reason_text = models.TextField()

class FakeVideo(models.Model):
    title = models.CharField(max_length=64)
    video = models.FileField(upload_to='deep-fake-videos')
    reasons = models.ManyToManyField(to=Reason, blank=True)
