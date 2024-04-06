from django.urls import path
import task_tracker.views as task_views 


urlpatterns = [
	path('', task_views.Index.as_view(), name='index'),
	path('tasks/', task_views.TaskListView.as_view(), name='task-list'),
	path('tasks/<int:pk>', task_views.TaskDetailView.as_view(), name='task-details'),
	path('task-create/', task_views.TaskCreateView.as_view(), name='task-create'),
	path('task-update/<int:pk>', task_views.TaskUpdateView.as_view(), name='task-update'),
	path('task-delete/<int:pk>', task_views.TaskDeleteView.as_view(), name='task-delete'),
]

app_name = "task-tracker"