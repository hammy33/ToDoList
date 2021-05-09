from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(next_page='Login'), name='Logout'),
    path('', TaskList.as_view(), name='Tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='Task'),
    path('create-task/', TaskCreate.as_view(), name='Create a Task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='Update Task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='Delete Task'),
]