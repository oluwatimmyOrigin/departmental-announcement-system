from django.db import models
from django.contrib.auth import get_user_model

from announcements.models import Announcement


# Create your models here.
class Notification(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
