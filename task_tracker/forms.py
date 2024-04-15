from django import forms
from .models import *


class TaskCreateForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ["name", "description", "status", "priority", "end_date"]


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ["content"]