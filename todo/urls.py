from django.urls import path 
from .views import TaskCreate, TaskDetail, TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='todo.index'),
    path('todo/<int:pk>/', TaskDetail.as_view(), name='todo.show'),
    path('todo/create/', TaskCreate.as_view(), name='todo.create'),
]
