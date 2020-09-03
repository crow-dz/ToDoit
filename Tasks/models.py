from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse ,reverse_lazy
class tasks(models.Model):
	task = models.CharField(max_length=100)
	completed = models.BooleanField(default=False)
	prioriteis=(
		('0','0'),
		('1','1'),
		('2','2'),
		('3','3'))
	priority = models.CharField(max_length=10,default='0',blank=True,null=True,choices=prioriteis)
	author = models.ForeignKey(User,on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse_lazy('user-tasks', kwargs={'username': self.author.username})
	








'''
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class tasks(models.Model):
	task = models.CharField(max_length=100)
	status = models.BooleanField(default=False)
	priority = models.IntegerField(default=0)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	def get_absolute_url(self):
		return reverse('home-page')
 
'''