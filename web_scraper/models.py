from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class Article(models.Model):
	detail_url = models.CharField(max_length=2048, unique=True)
	title = models.CharField(max_length=1024)
	image = models.CharField(max_length=2048)
	likes = models.CharField(max_length=20)
	responses = models.CharField(max_length=20)
	tags = ArrayField(ArrayField(models.CharField(max_length=2048, blank=True, null=True), null=True, blank=True),
					  null=True, blank=True)
	creator = models.CharField(max_length=100)
	creator_image = models.CharField(max_length=2048)

	def __str__(self):
		return str(self.id)


class ArticleDetail(models.Model):
	url = models.CharField(max_length=3062, unique=True)
	title = models.CharField(max_length=1024)
	image = models.CharField(max_length=2048)
	likes = models.CharField(max_length=20)
	responses = models.CharField(max_length=20)
	tags = ArrayField(ArrayField(models.CharField(max_length=2048), null=True, blank=True), null=True, blank=True)
	paragraph = ArrayField(ArrayField(models.TextField(), null=True, blank=True), null=True, blank=True)
	creator = models.CharField(max_length=100)
	creator_image = models.CharField(max_length=2048)

	def __str__(self):
		return str(self.id)
