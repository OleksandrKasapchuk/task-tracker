from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic import View, ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .mixins import *



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

	def get_queryset(self):
		return Task.objects.filter(dashboard_id=self.kwargs['dashboard_pk'])
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['dashboard_pk'] = self.kwargs['dashboard_pk']
		return context

class TaskDetailView(DetailView):
	model = Task
	context_object_name = "task"
	template_name = "task_tracker/task_details.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['dashboard_pk'] = self.kwargs['dashboard_pk']
		return context




class TaskCreateView(LoginRequiredMixin, CreateView):
	model = Task
	template_name = "task_tracker/task_form.html"
	form_class = TaskCreateForm

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.dashboard = Dashboard.objects.get(id=self.kwargs['dashboard_pk'])
		return super().form_valid(form)
	def get_success_url(self) -> str:
		return reverse_lazy("task-tracker:task-list",  kwargs={'dashboard_pk': self.kwargs['dashboard_pk']})


class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
	model = Task
	template_name = "task_tracker/task_form.html"
	context_object_name = "task"
	form_class = TaskCreateForm
	def get_success_url(self) -> str:
		return reverse_lazy("task-tracker:task-list",  kwargs={'dashboard_pk': self.kwargs['dashboard_pk']})


class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
	model = Task
	template_name = "task_tracker/task_form.html"
	def get_success_url(self) -> str:
		return reverse_lazy("task-tracker:task-list",  kwargs={'dashboard_pk': self.kwargs['dashboard_pk']})
