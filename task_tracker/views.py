from django.forms import BaseModelForm
from django.http import HttpResponse
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

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['dashboard_pk'] = self.kwargs['dashboard_pk']
		context['form'] = FilterTaskForm(self.request.GET)
		return context
	def get_queryset(self):
		queryset = super().get_queryset()
		priority = self.request.GET.get("priority", "")
		if priority:
			if priority == "4":
				queryset = queryset.all()
			else:
				queryset = queryset.filter(priority=priority)
		return queryset.filter(dashboard_id=self.kwargs['dashboard_pk'])

class TaskDetailView(DetailView):
	model = Task
	context_object_name = "task"
	template_name = "task_tracker/task_details.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['dashboard_pk'] = self.kwargs['dashboard_pk']
		task = self.get_object()
		context['comments'] = Comment.objects.filter(task=task)
		return context


class TaskCreateView(LoginRequiredMixin, CreateView):
	model = Task
	template_name = "task_tracker/task_form.html"
	form_class = TaskCreateForm

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.dashboard = Dashboard.objects.get(id=self.kwargs['dashboard_pk'])
		form.instance.end_date = form.cleaned_data['end_date']
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


class AddCommentView(LoginRequiredMixin, CreateView):
	model = Comment
	template_name = "task_tracker/comment.html"
	form_class = CommentForm
	def form_valid(self, form: BaseModelForm) -> HttpResponse:
		form.instance.creator = self.request.user
		form.instance.task = Task.objects.get(id=self.kwargs['pk'])
		return super().form_valid(form)
	def get_success_url(self) -> str:
		return reverse_lazy("task-tracker:task-details",  kwargs={'dashboard_pk': self.kwargs['dashboard_pk'],"pk":self.kwargs['pk']})