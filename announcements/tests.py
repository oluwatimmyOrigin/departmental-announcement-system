from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

from .models import Announcement

from datetime import timedelta


# Create your tests here.
class AnnouncementTestCase(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create(
            username='testuser',
            email='testuser@email.com',
            is_staff=True,
        )

        self.announcement = Announcement.objects.create(
            title='Test Announcement',
            content='This is a test announcement!',
            category='news',
            posted_by=self.admin_user,
            expiration_date=timezone.now() + timedelta(days=2),
        )

        self.client = Client()

    def test_announcement_setup(self):
        self.assertEqual(str(self.announcement), 'Test Announcement')
        self.assertEqual(self.announcement.posted_by, self.admin_user)

    def test_announcement_create(self):
        data = {
            'title': 'Welcome back to school!',
            'content': 'It\'s the beginning of a new semester! Hurrayyyy!!!!',
            'expiration_date': timezone.now() + timedelta(days=3)
        }

        response = self.client.post(reverse('announcements:create'), data=data)

        self.assertEqual(response.status_code, 302)

    def test_check_reservation_url(self):
        response = self.client.get(reverse('announcements:list'))

        self.assertEqual(response.status_code, 200)
