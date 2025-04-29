from django.urls import path

from . import views


app_name = 'announcements'

urlpatterns = [
    path('', views.AnnouncementListView.as_view(), name='list'),
    path('create/', views.AnnouncementCreateView.as_view(), name='create'),
    path('<slug:slug>/', views.AnnouncementDetailView.as_view(), name='detail'),
]
