from django.urls import path
from artportal.art_auth.views import login_user, logout_user, UserDelete, \
    RegisterView, AccountDetailsView

urlpatterns = (
    path('login/', login_user, name="log in user"),
    path('logout/', logout_user, name="log out user"),
    path('register/', RegisterView.as_view(), name="register user"),
    path('view/', AccountDetailsView.as_view(), name="view profile details"),
    path('<int:pk>/delete', UserDelete.as_view(), name='user confirm delete')

)