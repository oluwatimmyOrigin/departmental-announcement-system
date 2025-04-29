from rest_framework.serializers import ModelSerializer

from .models import Announcement


class AnnouncementListSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        field = '__all__'


class AnnouncementCreateSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        exclude = ['posted_by', 'date_created']
