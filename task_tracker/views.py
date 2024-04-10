from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *


class Index(TemplateView):
	template_name = "task_tracker/index.html"


class DashboardListView(ListView):
	model = Dashboard
	context_object_name = "dashboards"
	template_name = "task_tracker/dashboards.html"


class TaskListView(ListView):
	model = Task
	context_object_name = "tasks"
	template_name = "task_tracker/tasks.html"


class TaskDetailView(DetailView):
	model = Task
	context_object_name = "task"
	template_name = "task_tracker/task_details.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
	model = Task
	template_name = "task_tracker/task_form.html"
	form_class = TaskCreateForm
	success_url = reverse_lazy("task-tracker:task-list")

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
	model = Task
	template_name = "task_tracker/task_form.html"
	context_object_name = "task"
	form_class = TaskCreateForm
	success_url = reverse_lazy("task-tracker:task-list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
	model = Task
	template_name = "task_tracker/task_form.html"
	success_url = reverse_lazy("task-tracker:task-list")