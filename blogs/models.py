from django.db import models
from profiles.models import Profile


class Blog(models.Model):
	name = models.CharField(max_length=60, default=True)
	authors = models.ManyToManyField(Profile)

	def __str__(self):
		return self.name

class Comment(models.Model):
	text = models.CharField(max_length=100)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=1)

	def __str__(self):
		return f"{self.blog.name} {self.text} "