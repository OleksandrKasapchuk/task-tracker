from django import forms
from .models import *


class DashboardCreateForm(forms.ModelForm):
	class Meta:
		model = Dashboard
		fields = ['name']
	
class TaskCreateForm(forms.ModelForm):
	end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)
	class Meta:
		model = Task
		fields = ["name", "description", "status", "priority"]


class FilterTaskForm(forms.Form):
	result1 = [("4", "All")]
	for i in Task.PRIORITY_CHOICES:
		result1.append(i)
	priority = forms.ChoiceField(choices=result1, required=False, label="Priority")



class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ["content", "media"]
		widjets = {
			"media": forms.FileInput()
		}