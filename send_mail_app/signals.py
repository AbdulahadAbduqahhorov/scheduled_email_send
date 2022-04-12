import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from send_mail_app.models import SendEmail


@receiver(post_save, sender=SendEmail)
def send_email_signal(sender, instance, created, **kwargs):
    if created:
        schedule, created = CrontabSchedule.objects.get_or_create(month_of_year=instance.scheduled_at.month,
                                                                  day_of_month=instance.scheduled_at.day,
                                                                  hour=instance.scheduled_at.hour,
                                                                  minute=instance.scheduled_at.minute)
        print(instance.scheduled_at.hour)
        PeriodicTask.objects.create(crontab=schedule,
                                    name=f'{instance.subject}',
                                    task='send_mail_app.tasks.send_mail_func',
                                    args=json.dumps(
                                        [instance.subject, instance.message]))
