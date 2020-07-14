from django.db import models

# Create your models here.

class Reason(models.Model):
    email = models.EmailField()
    age = models.PositiveIntegerField()
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    ]
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    ethnicity = models.CharField(max_length=64)
    REAL = 'R'
    FAKE = 'F'
    UNSURE = 'U'
    VIDEO_TYPE_CHOICES = [
        (REAL, 'Real'),
        (FAKE, 'Fake'),
        (UNSURE, 'Unsure'),
    ]
    video_type = models.CharField(
        max_length=2,
        choices=VIDEO_TYPE_CHOICES,
        default=REAL,
    )
    reason_text = models.TextField(help_text='Please mention in detail why you think the video is real/fake.')
    reason_keywords = models.CharField(
        max_length=128,
        help_text='Please enter the keywords that describe your choice in not more than 10 words.'
    )

class FakeVideo(models.Model):
    title = models.CharField(max_length=64)
    video = models.FileField(upload_to='deep-fake-videos')
    reasons = models.ManyToManyField(to=Reason, blank=True)
