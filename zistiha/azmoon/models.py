from __future__ import unicode_literals
# - *- coding: utf- 8 - *-

from django.db import models

class Exam(models.Model):
	"""docstring for Exam"""
	title = models.CharField(max_length=50)
	start=models.DateTimeField()
	duration=models.IntegerField(default=60)
	link=models.CharField(max_length=50)
	image=models.ImageField()
	cost=models.IntegerField(default=0)
	key=models.CharField(max_length=500, default="1-2 2-3 3-3 4-2")

class ExamOrder(models.Model):
	exam = models.ForeignKey(Exam, null=True,on_delete=models.SET_NULL)
	name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	phone_number=models.CharField(max_length=20)
	school_type=models.CharField(max_length=30,default="unknown")
	school_name=models.CharField(max_length=30,default="unknown")
	city=models.CharField(max_length=30,default="unknown")
	provinence=models.CharField(max_length=30,default="unknown")
	seckey=models.CharField(max_length=10)
	payed=models.BooleanField(default=False)
	session=models.CharField(max_length=20,default='not_valid')
	examsnumber=models.IntegerField(default=1)
	ordersnumber=models.IntegerField(default=1)

class ExamSubmition(models.Model):
	order=models.ForeignKey(ExamOrder,null=True,on_delete=models.SET_NULL)
	score=models.IntegerField(default=0)
	rank=models.IntegerField(default=1)
	exam=models.ForeignKey(Exam,null=True,on_delete=models.SET_NULL)
	submitted=models.CharField(max_length=500,default="salam")


class Bonus(models.Model):
	submition=models.OneToOneField(ExamSubmition,unique=True)
	percent=models.IntegerField(default=0)
	code=models.CharField(max_length=10,default="notvalid")
	used=models.BooleanField(default=False)

class Course(models.Model):
	title=models.CharField(max_length=100)
	Description=models.TextField(default="nothing!",null=True)
	cost=models.IntegerField(default=0)
	start=models.DateTimeField()


class CourseOrder(models.Model):
	course=models.ForeignKey(Course)
	name=models.CharField(max_length=20,default="None")
	last_name=models.CharField(max_length=20)
	phone_number=models.CharField(max_length=20)
	school_type=models.CharField(max_length=30,default="unknown")
	school_name=models.CharField(max_length=30,default="unknown")
	city=models.CharField(max_length=30,default="unknown")
	provinence=models.CharField(max_length=30,default="unknown")
	parent_phone=models.CharField(max_length=20,null=True)
	Bonus=models.ForeignKey(Bonus,null=True)	
	payment_type=models.CharField(max_length=10,default="once")
	
	rest_money=models.FloatField(default=0)
	order_date=models.DateTimeField(auto_now=True)
	payed=models.BooleanField(default=False)
	should_pay=models.FloatField(default=0)
	session=models.CharField(max_length=20,default='not_valid')

	ordersnumber=models.IntegerField(default=1)

		
class Payments(models.Model):
	code=models.CharField(max_length=50)
		
class HotelReserve(models.Model):
	name=models.CharField(max_length=20,default="None")
	last_name=models.CharField(max_length=20)
	phone_number=models.CharField(max_length=20)
	parent_phone=models.CharField(max_length=20,null=True)
	home_phone=models.CharField(max_length=20)
	city=models.CharField(max_length=30,default="unknown")
	provinence=models.CharField(max_length=30,default="unknown")
	sid=models.CharField(max_length=20)

	orderDate=models.DateTimeField(auto_now=True)
	course=models.ForeignKey(Course,default=None)
	payed=models.BooleanField(default=False)
	ordersnumber=models.IntegerField(default=1)
	session=models.CharField(max_length=20,default="not valid")

class PrintObject(models.Model):
	text=models.TextField()
	print_id=models.CharField(max_length=40,default="not_valid")
		






