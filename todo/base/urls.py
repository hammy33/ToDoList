from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name='Tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='Task'),
    path('create-task/', TaskCreate.as_view(), name='Create a Task'),
]