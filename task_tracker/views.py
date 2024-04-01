from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .forms import *


class Index(TemplateView):
	template_name = 'task_tracker/index.html'


class TaskListView(ListView):
	model = Task
	context_object_name = 'tasks'
	template_name = "task_tracker/tasks.html"


class TaskDetailView(DetailView):
	model = Task
	context_object_name = "task"
	template_name = "task_tracker/task_details.html"


class TaskCreateView(CreateView):
	model = Task
	template_name = "task_tracker/task_form.html"
	form_class = TaskCreateForm
	success_url = reverse_lazy("task_tracker:task-list")