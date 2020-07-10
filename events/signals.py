from django.conf import settings
from celery import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from main_app import models, tasks

@receiver(post_save, sender = models.Event)
def send_mail(sender, instance = None, created = False, **kwargs):
    if created:
        email = instance.user.email
        datetime = instance.datetime_end
        title = instance.title
        tasks.send_event_mail.delay(email, datetime, title)
