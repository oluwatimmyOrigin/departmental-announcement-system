from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class AnnouncementCategory(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Announcement(models.Model):
    CATEGORY_CHOICES = (
        ('events', 'Events'),
        ('news', 'News'),
        ('reminders', 'Reminders')
    )
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, default='news', max_length=30)
    posted_by = models.ForeignKey(get_user_model(), limit_choices_to={'is_staff': True}, on_delete=models.SET_NULL, null=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('announcements:detail', args=[self.slug])

    @property
    def is_expired(self):
        return self.expiration_date < timezone.now() if self.expiration_date else False
