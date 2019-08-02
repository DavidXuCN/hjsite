from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class IMG (models.Model):
	img = models.ImageField(upload_to='img')
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '图片'
		verbose_name_plural = verbose_name

class Category (models.Model):
	name = models.CharField(max_length=80)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '分类'
		verbose_name_plural = verbose_name

class Tag (models.Model):
	name = models.CharField(max_length=80)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '标签'
		verbose_name_plural = verbose_name

class Post (models.Model):	
	title = models.CharField(max_length=80)
	subtitle = models.CharField(max_length=200, blank=True)
	publish_date = models.DateTimeField()
	preview_content = models.TextField()
	content = models.TextField()
	link = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tag = models.ManyToManyField(Tag, blank=True)			
	img = models.ForeignKey(IMG, on_delete=models.CASCADE, blank=True)	
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '文章'
		verbose_name_plural = verbose_name

	




