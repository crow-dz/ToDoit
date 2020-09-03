from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
	"""docstring for ClassName"""
	email = forms.EmailField()


	CHOICES=[('Male','Male'),
				('Female','Female')]
	gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
	class Meta:
		model = User
		fields = ['username','gender','email','password1','password2']	

class UserUpdateForm(forms.ModelForm):
	"""docstring for UserUpdateForm"""
	email = forms.EmailField()

	class Meta:
		model = User
		fields =['username','email']

class UserUpdateName(forms.ModelForm):
	firstName = forms.CharField(max_length=30)
	LastName = forms.CharField(max_length=30)

	class Meta:
			model = User
			fields =['firstName','LastName']	