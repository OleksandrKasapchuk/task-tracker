from django import forms
from .models import *


class TaskCreateForm(forms.ModelForm):
	end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local',}))
	class Meta:
		model = Task
		fields = ["name", "description", "status", "priority"]


class FilterTaskForm(forms.Form):
	result = [("4", "All")]
	for i in Task.PRIORITY_CHOICES:
		result.append(i)
	priority = forms.ChoiceField(choices=result, required=False, label="Priority")


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ["content"]