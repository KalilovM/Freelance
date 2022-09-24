from rest_framework import serializers
from .models import *

class LinksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Links
		fields = '__all__'


class MessngerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Messenger
		fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
	links = LinksSerializer()
	messengers = MessngerSerializer()
	slug = serializers.SlugField()

	class Meta:
		model = CustomUser
		fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
	slug = serializers.SlugField()
	class Meta:
		model = Skill
		fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
	slug = serializers.SlugField()
	class Meta:
		model = Category
		fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
	category = CategorySerializer()

	class Meta:
		model = Activity
		fields = '__all__'


class SalarySerializer(serializers.HyperlinkedModelSerializer):
	pay_method = serializers.MultipleChoiceField(choices=methods)
	salary_per = serializers.MultipleChoiceField(choices=options)
	ownership = serializers.MultipleChoiceField(choices=ownerships)
	class Meta:
		model = Salary
		fields = '__all__'


class FreelancerSerializer(serializers.ModelSerializer):
	activities = ActivitySerializer()
	skills = SkillSerializer()
	salary = SalarySerializer()

	class Meta:
		model = Freelancer
		fields = '__all__'


class CustomerSerializer(CustomUserSerializer):
	class Meta:
		model = Customer
		fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
	user = CustomUserSerializer
	class Meta:
		model = Review
		fields = '__all__'