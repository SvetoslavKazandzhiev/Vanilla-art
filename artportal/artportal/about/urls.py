from django.urls import path

from artportal.about.views import about_view

urlpatterns = (
    path('about/', about_view, name='about'),
)