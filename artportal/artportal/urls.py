from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('artportal.art_app.urls')),
                  path('auth/', include('artportal.art_auth.urls')),
                  path('profiles/', include('artportal.profiles.urls')),
                  path('topics/', include('artportal.topics.urls')),
                  path('about/', include('artportal.about.urls')),
                  path('contact/', include('artportal.contact.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
