from django.urls import path
from . import views
from .views import edit_art, ArtDetailsView, CommentArtView, CreateArtView, DeleteArtView

urlpatterns = (
    path('', views.IndexView.as_view(), name="index"),
    path('create/', CreateArtView.as_view(), name="create"),
    path('edit/<int:pk>', edit_art, name='edit art'),
    path('delete/<int:pk>', DeleteArtView.as_view(), name='delete art'),
    path('details/<int:pk>', ArtDetailsView.as_view(), name='details art img'),
    path('comment/<int:pk>', CommentArtView.as_view(), name='comment pet'),
)
