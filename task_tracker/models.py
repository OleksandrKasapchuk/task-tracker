from django.db import models
from auth_system.models import CustomUser

class Task(models.Model):

	STATUS_CHOICES = [
		("todo", "To Do"),
		("progress", "In Progress"),
		("done", "done")
	]
	PRIORITY_CHOICES = [
		("low", "Low"),
		("medium", "Medium"),
		("high", "High")
	]
	name = models.CharField(max_length=50)
	description = models.TextField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
	priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
	end_date = models.DateField(null=True, blank=True)
	creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks")


	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ("status", "end_date")
		verbose_name = "task"
		verbose_name_plural = "tasks"