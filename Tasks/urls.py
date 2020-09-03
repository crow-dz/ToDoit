from django.urls import path 
from . import views
from . views import TaskListView,TaskCreateView,TaskUpadteView,UserTaskListView




urlpatterns = [
	
	path('', views.index,name='index-page'),
    path('task/', views.TaskListView.as_view(),name='home-page'),
    path('task/new/', views.TaskCreateView.as_view(),name='create-task'),
    path('task/<int:pk>/update/', views.TaskUpadteView.as_view(),name='update-task'), 
    path('task/<int:pk>/delete/', views.UserDeleteView.as_view(),name='delete-task'), 
    path('user/<str:username>', views.UserTaskListView.as_view(),name='user-tasks')   

]