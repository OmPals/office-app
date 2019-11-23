
import smtplib 
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from phone_field import PhoneField

# s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
# s.starttls() 
# Authentication /
# s.login("####@gm.com", "####") 

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
	# host_addr= models.CharField(max_length = 500, blank = True)
	def __str__(self):
		return self.name

class Visit(models.Model):
	visitor= models.ForeignKey(Visitor, on_delete=models.CASCADE)
	host= models.ForeignKey(Host, on_delete=models.CASCADE)
	check_in= models.DateTimeField()
	check_out= models.DateTimeField()
	visit_addr= models.CharField(max_length = 500, blank = True)
	listc = [('0', 'not sent'), ('1', 'already sent'), ('2', 'send now!!')]
	send_mail_opt = models.CharField(max_length = 15, choices = listc, default = '0')
	# message = str(check_in) + str(check_out) + visit_addr
	# if(check_out != NULL)
	# actions = s.sendmail("####", visitor.getMail(), message)

# s.quit()