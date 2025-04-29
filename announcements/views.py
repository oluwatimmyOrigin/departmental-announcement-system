
from .models import Announcement
from .forms import AnnouncementForm

from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse

from datetime import date


# Create your views here.
class AnnouncementCreateView(UserPassesTestMixin, CreateView):
    model = Announcement
    form_class =  AnnouncementForm
    queryset = Announcement.objects.all()
    template_name = 'announcements/announcements_create.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse('announcements:list')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user

        return super().form_valid(form)


class AnnouncementListView(ListView):
    model = Announcement
    queryset = Announcement.objects.all()
    paginate_by = 5
    paginate_orphans = 2
    template_name = 'announcements/announcements_list.html'
    context_object_name = 'announcements'


class AnnouncementDetailView(DetailView):
    model = Announcement
    queryset = Announcement.objects.all()
    context_object_name = 'announcement'
    template_name = 'announcements/announcements_detail.html'
