from django.urls import path 
from .views import TaskCreate, TaskDetail, TaskList, TaskEdit, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='todo.login'),
    path('logout/', LogoutView.as_view(next_page='todo.login'), name='todo.logout'),
    path('register/', RegisterPage.as_view(), name='todo.register'),

    path('', TaskList.as_view(), name='todo.index'),
    path('todo/<int:pk>/', TaskDetail.as_view(), name='todo.show'),
    path('todo/create/', TaskCreate.as_view(), name='todo.create'),
    path('todo/edit/<int:pk>/', TaskEdit.as_view(), name='todo.edit'),
    path('todo/delete/<int:pk>/', TaskDelete.as_view(), name='todo.delete'),
]
