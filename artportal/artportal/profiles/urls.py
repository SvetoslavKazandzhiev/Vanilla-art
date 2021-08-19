from django.urls import path

from artportal.profiles.views import profile_details, view_profile

urlpatterns = (
    path('', profile_details, name='profile details'),
    path('view/', view_profile, name='view profile'),
)

import artportal.profiles.signals