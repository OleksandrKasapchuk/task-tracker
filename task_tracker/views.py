from django.shortcuts import render, redirect, reverse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .forms import *


class Index(TemplateView):
	pass


class TaskListView(ListView):
	model = Task
	context_object_name = 'tasks'
	template_name = "task_tracker/tasks.html"


class TaskDetailView(DetailView):
	model = Task
	context_object_name = "task"
	template_name = "task_tracker/task_details.html"


# class TaskCreateView(CreateView):
# 	model = Task
# 	template_name = "task_tracker/task_form.html"
# 	form_class = TaskCreateForm
# 	success_url = reverse("task_tracker:tasks")