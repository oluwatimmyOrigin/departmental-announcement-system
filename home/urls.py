from django.urls import path
from django.contrib.auth import views as auth_views

from announcements.views import AnnouncementListView


urlpatterns = [
    path('', AnnouncementListView.as_view(), name='homepage'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'), # TODO: Add login template
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
