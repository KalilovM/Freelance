from django.db import models


class Order(models.Model):
	statuses = (
		(1, "В поиске"),
		(2, "Фрилансер назначен"),
		(3, "Завершено"),
	)
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)
	files = models.FileField(upload_to="order/%Y/%m/%d/")
	category = models.ManyToManyField('users.Category')
	skills = models.ManyToManyField('users.Skill')
	reward = models.ForeignKey('orders.Reward', on_delete=models.SET_NULL,null=True)
	promotion = models.ManyToManyField('Promotion', blank=True)
	status = models.CharField(choices=statuses,max_length=20)
	freelancer = models.ForeignKey('users.Freelancer', on_delete=models.PROTECT, blank=True)
	responses = models.ManyToManyField('orders.Response')
	customer = models.ForeignKey('users.Customer', on_delete=models.PROTECT)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField()


class Reward(models.Model):
	options = (
		(1, "За проект"),
		(2, "За час"),
	)
	price = models.IntegerField(blank=True)
	option = models.CharField(choices=options, blank=True,max_length=10)
	is_negotiable = models.BooleanField(default=False)


class Promotion(models.Model):
	image = models.ImageField(upload_to="promotion/")
	title = models.CharField(max_length=50)
	details = models.CharField(max_length=255)
	cost = models.IntegerField()

	def __str__(self):
		return self.title


class Response(models.Model):
	response = models.CharField(max_length=200, blank=True)
	freelancer = models.ForeignKey('users.Freelancer', on_delete=models.CASCADE)

	def __str__(self):
		return self.freelancer.username
