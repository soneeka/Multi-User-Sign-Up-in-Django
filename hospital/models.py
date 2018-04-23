from django.db import models
from django.contrib.auth.models import User
# Create your models here.
DEPARTMENT=(
	('pathology','pathology'),
	('cardiology','cardiology'),
	('physiology','physiology'),
	)
class  Staff(User):
	name = models.CharField(max_length=200)
	department=models.CharField(max_length=20,choices=DEPARTMENT, blank = True)
	

	def __str__ (self):
	 	return '{} : {}'.format(self.name,self.department)

class  Doctor(User):
	name = models.CharField(max_length=200)
	department=models.CharField(max_length=20,choices=DEPARTMENT, blank = True)
	academic=models.CharField(max_length=50)


	def __str__ (self):
	 	return ' {} :{}'.format(self.name,self.department)

class  Patient(User):
	name = models.CharField(max_length=200)
	symptoms= models.CharField(max_length=500, blank=True)

	def __str__ (self):
	 	return '{}'.format(self.name)

class Post(models.Model):
	post = models.CharField(max_length=500)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True)
	medicines=models.CharField(max_length=100)
	# updated= models.DateTimeField(auto_now=True)