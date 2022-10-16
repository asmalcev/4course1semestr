from django.db import models
from datetime import datetime
from django.contrib import admin



class News(models.Model):
	publication_date = models.DateTimeField(default=datetime.now, blank=True)
	title = models.CharField(max_length=128)
	content = models.TextField(max_length=1024)

	def __str__(self):
		return '{} {}'.format(self.publication_date.date(), self.title)


admin.site.register(News)