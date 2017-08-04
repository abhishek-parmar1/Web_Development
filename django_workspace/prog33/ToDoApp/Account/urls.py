from django.conf.urls import url
from views import UserListView , UserCreateView

urlpatterns = [
    url('^list', UserListView.as_view()),
    url('^create', UserCreateView.as_view())
]