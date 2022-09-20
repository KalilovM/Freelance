from django.db import models
from users.models import Skill, Category, Freelacer, Customer


class Order(models.Model):
	statuses = (
		(1, "В поиске"),
		(2, "Фрилансер назначен"),
		(3, "Завершено"),
	)
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)
	files = models.FileField(upload_to="order/%Y/%m/%d/")
	category = models.ManyToManyField('Category')
	skills = models.ManyToManyField('Skill')
	reward = models.ForeignKey('Revard', on_delete=models.SET_NULL)
	promotion = models.ManyToManyField('Promotion', blank=True)
	status = models.CharField(choices=statuses)
	freelancer = models.ForeignKey('Freelacer', on_delete=models.PROTECT, blank=True)
	responces = models.ManyToManyField()
	customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField()


class Revard(models.Model):
	options = (
		(1, "За проект"),
		(2, "За час"),
	)
	price = models.IntegerField(blank=True)
	option = models.CharField(choices=options, blank=True)
	is_negotiable = models.BooleanField(default=False)


class Promotion(models.Model):
	image = models.ImageField(upload_to="promotion/")
	title = models.CharField(max_length=50)
	details = models.CharField(max_length=255)
	cost = models.IntegerField()

	def __str__(self):
		return self.title


class Responce(models.Model):
	response = models.CharField(max_length=200, blank=True)
	freelancer = models.ForeignKey('Freelancer', on_delete=models.CASCADE)

	def __str__(self):
		return self.freelancer.username
