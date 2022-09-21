from django.db import models


class Service(models.Model):
	title = models.CharField(max_length=70)
	description = models.TextField()
	freelancer = models.ForeignKey('users.Freelancer', on_delete=models.CASCADE)
	category = models.ForeignKey('users.Category', on_delete=models.PROTECT)
	price = models.IntegerField()
	skills = models.ManyToManyField('users.Skill')
	projects = models.ManyToManyField('services.Project')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField()

	def __str__(self):
		return self.title + " " + self.freelancer.username


class Project(models.Model):
	freelancer = models.ForeignKey('users.Freelancer', on_delete=models.CASCADE)
	title = models.CharField(max_length=70)
	category = models.ForeignKey('users.Category', on_delete=models.SET_NULL, null=True)
	cover = models.ImageField(upload_to='project/covers/%Y/%m/%d/')
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title + " " + self.freelancer.username


class ProjectImages(models.Model):
	project = models.ForeignKey('services.Project', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='project/%Y/%m/%d/')
