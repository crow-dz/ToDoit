from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	firstName = models.CharField(default='firstName',max_length=30)
	LastName = models.CharField(default='LastName',max_length=30)

	def __str__(self):
		return f'{self.user.username} Profile'
