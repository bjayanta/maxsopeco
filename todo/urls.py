from django.urls import path 
from .views import TaskDetail, TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='todo.index'),
    path('todo/<int:pk>/', TaskDetail.as_view(), name='todo.show'),
]
