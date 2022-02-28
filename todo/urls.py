from django.urls import path 
from .views import TaskCreate, TaskDetail, TaskList, TaskEdit, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='todo.index'),
    path('todo/<int:pk>/', TaskDetail.as_view(), name='todo.show'),
    path('todo/create/', TaskCreate.as_view(), name='todo.create'),
    path('todo/edit/<int:pk>/', TaskEdit.as_view(), name='todo.edit'),
    path('todo/delete/<int:pk>/', TaskDelete.as_view(), name='todo.delete'),
]
