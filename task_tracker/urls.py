from django.urls import path
import task_tracker.views as task_views 


urlpatterns = [
	path('', task_views.Index.as_view(), name='index'),
	path('dashboards/', task_views.DashboardListView.as_view(), name='dashboard-list'),
	path('dashboards/<int:dashboard_pk>/tasks/', task_views.TaskListView.as_view(), name='task-list'),
	path('dashboards/<int:dashboard_pk>/tasks/<int:pk>', task_views.TaskDetailView.as_view(), name='task-details'),
	path('dashboards/<int:dashboard_pk>/task-create/', task_views.TaskCreateView.as_view(), name='task-create'),
	path('dashboards/<int:dashboard_pk>/task-update/<int:pk>', task_views.TaskUpdateView.as_view(), name='task-update'),
	path('dashboards/<int:dashboard_pk>/task-delete/<int:pk>', task_views.TaskDeleteView.as_view(), name='task-delete'),
]

app_name = "task-tracker"