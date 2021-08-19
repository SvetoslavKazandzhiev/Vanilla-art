from django.urls import path
from . import views
from .views import topic_type, topic_type_other, topic_type_fine_art, topic_type_jewellery, topic_type_photography

urlpatterns =(
    path('', views.TopicsView.as_view(), name="topics"),
    path('more/graphic', topic_type, name="more topic graphic"),
    path('more/other', topic_type_other, name="more topic other"),
    path('more/fine-art', topic_type_fine_art, name="more topic fine art"),
    path('more/jewellery', topic_type_jewellery, name="more topic jewellery"),
    path('more/photography', topic_type_photography, name="more topic photography"),
)