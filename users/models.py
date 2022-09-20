from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	# Todo сделать валидацию изображения (размер, разрешение)
	image = models.ImageField(upload_to="user_pictures/%Y/%m/%d/", null=True, blank=True,
	                          default="user_pictures/default.jpg")
	birth_date = models.DateTimeField(null=True, blank=True)
	location = models.CharField(max_length=30, blank=True)
	phone = models.CharField(max_length=30, blank=True)
	email_contact = models.CharField(max_length=50, blank=True)
	links = models.ManyToManyField('Links',blank=True)
	messagers = models.ManyToManyField('Messager',blank=True)

	# Todo сделать верификацию пользователя

	class Meta:
		ordering = ['-created', 'username']

	def __str__(self):
		return self.username


class freelacer(CustomUser):
	exp = (
		(1, 'Менее года'),
		(2, 'Более года'),
		(3, 'Более трех лет'),
		(4, 'Более пяти лет'),
		(5, 'Более 10 лет'),
	)
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	profession = models.CharField(max_length=70, blank=True)
	bio = models.TextField(max_length=500, blank=True)
	work_experience = models.CharField(choices=exp, blank=True)
	activities = models.ManyToManyField('Activity', blank=True)
	skills = models.ManyToManyField('Skill', blank=True)
	salary = models.ForeignKey('Salary', blank=True)
	is_published = models.BooleanField(default=True)
	# Todo добавить приложение проекты которые будут включать в себя отдельный раздел связанный с пользователем

	slug = models.SlugField()

	class Meta:
		ordering = ['-created', 'username']

	def __str__(self):
		return self.username


class Customer(CustomUser):
	user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	class Meta:
		ordering = ['-created', 'username']

	def __str__(self):
		return self.username


class Activity(models.Model):
	title = models.CharField(max_length=70)
	category = models.ForeignKey('Category', on_delete=models.SET_NULL)

	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title


class Skill(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Salary(models.Model):
	options = (
		(1, "За час"),
		(2, "За месяц"),
		(3, "За тысячу знаков"),
		(4, "За проект"),
	)
	methods = (
		(1, "наличный расчет"),
		(2, "безналичный расчет"),
		(3, "электронные деньги"),
	)
	ownerships = (
		(1, "Юр. лицо"),
		(2, "ИП"),
		(3, "Физ. лицо"),
	)
	salary = models.IntegerField(max_length=20, blank=True)
	salary_per = models.CharField(choices=options, blank=True)
	pay_method = models.CharField(choices=methods, blank=True)
	ownership = models.CharField(choices=ownerships, blank=True)

	def __str__(self):
		return f'{self.salary} {self.pay_method}'


class Links(models.Model):
	link = models.CharField(max_length=70, blank=True)


class Messager(models.Model):
	choices = (
		(1, "Whatsapp"),
		(1, "Telegram"),
		(1, "Skype"),
		(1, "ICQ"),
		(1, "Jabber"),
	)
	messager = models.CharField(choices=choices, blank=True, default=1)
	number = models.CharField(max_length=50, blank=True)


