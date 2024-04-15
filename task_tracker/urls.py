from django.urls import path
import task_tracker.views as task_views 


urlpatterns = [
	path('', task_views.Index.as_view(), name='index'),
	path('dashboards/', task_views.DashboardListView.as_view(), name='dashboard-list'),
	path('dashboards/<int:dashboard_pk>/tasks/', task_views.TaskListView.as_view(), name='task-list'),
	path('dashboards/<int:dashboard_pk>/tasks/<int:pk>', task_views.TaskDetailView.as_view(), name='task-details'),
	path('dashboards/<int:dashboard_pk>/task-create', task_views.TaskCreateView.as_view(), name='task-create'),
	path('dashboards/<int:dashboard_pk>/task-edit/<int:pk>', task_views.TaskUpdateView.as_view(), name='task-edit'),
	path('dashboards/<int:dashboard_pk>/task-delete/<int:pk>', task_views.TaskDeleteView.as_view(), name='task-delete'),
	path('dashboards/<int:dashboard_pk>/tasks/<int:pk>/comment-add', task_views.AddCommentView.as_view(), name='comment-add')
]

app_name = "task-tracker"