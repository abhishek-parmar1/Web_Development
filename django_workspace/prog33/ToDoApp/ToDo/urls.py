from django.conf.urls import url
from views import TodoListView, TodoCreateView

urlpatterns = [
    url('^list', TodoListView.as_view()),
    url('^create', TodoCreateView.as_view())
]