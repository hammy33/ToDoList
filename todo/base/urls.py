from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='Tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='Task'),
    path('create-task/', TaskCreate.as_view(), name='Create a Task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='Update Task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='Delete Task'),
]