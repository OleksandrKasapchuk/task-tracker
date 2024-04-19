from django.db import models
from auth_system.models import CustomUser


class Dashboard(models.Model):
	name = models.CharField(max_length=100)
	users = models.ManyToManyField(CustomUser)

	def __str__(self):
		return self.name


class Task(models.Model):

	STATUS_CHOICES = [
		("1", "To Do"),
		("2", "In Progress"),
		("3", "done")
	]
	PRIORITY_CHOICES = [
		("1", "Low"),
		("2", "Medium"),
		("3", "High")
	]

	name = models.CharField(max_length=50)
	description = models.TextField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
	priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
	end_date = models.DateTimeField(null=True, blank=True)
	creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks")
	dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name="tasks")

	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ("status", "end_date")
		verbose_name = "task"
		verbose_name_plural = "tasks"


class Comment(models.Model):
	content = models.TextField()
	creator = models.ForeignKey(CustomUser,  on_delete=models.CASCADE,related_name="comments")
	task = models.ForeignKey(Task, on_delete=models.CASCADE,related_name="comments")