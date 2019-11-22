
from django.conf import settings
from django.db import models
from django.utils import timezone
from phone_field import PhoneField


class Visitor(models.Model):
	name= models.CharField(max_length = 128, blank = True)
	email= models.EmailField(max_length = 254, blank = True)
	phone= PhoneField(blank=True, help_text='Contact phone number')
	def __str__(self):
		return self.name

class Host(models.Model):
	name= models.CharField(max_length=128, blank = True)
	visits= models.ManyToManyField(Visitor, through='Visit')
	email= models.EmailField(max_length = 254, blank = True)
	phone= PhoneField(blank=True, help_text='Contact phone number')
	host_addr= models.CharField(max_length = 128, blank = True)
	def __str__(self):
		return self.name

class Visit(models.Model):
	visitor= models.ForeignKey(Visitor, on_delete=models.CASCADE)
	host= models.ForeignKey(Host, on_delete=models.CASCADE)
	check_in= models.DateTimeField()
	check_out= models.DateTimeField()
	visit_addr= models.CharField(max_length = 128, blank = True)
    # date_joined = models.DateField()
    # invite_reason = models.CharField(max_length=640)