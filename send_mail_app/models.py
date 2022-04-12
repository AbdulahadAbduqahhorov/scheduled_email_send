from django.db import models
from django_celery_beat.models import PeriodicTask, CrontabSchedule


class RecieverEmail(models.Model):
    user_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user_email


class SendEmail(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    to_email = models.ManyToManyField(to=RecieverEmail)
    scheduled_at = models.DateTimeField()

    def __str__(self):
        return self.subject
