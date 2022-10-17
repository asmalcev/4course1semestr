from django.db import models
from datetime import datetime
from django.contrib import admin
from django.contrib.auth.models import User



class News(models.Model):
	publication_date = models.DateTimeField(default=datetime.now, blank=True)
	title = models.CharField(max_length=128)
	content = models.TextField(max_length=1024)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return '{} {}'.format(self.publication_date.date(), self.title)


admin.site.register(News)