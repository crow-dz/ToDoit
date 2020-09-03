from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterForm , UserUpdateForm ,UserUpdateName
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse
def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('Profile-page')
	else:
		form = RegisterForm()
	return render(request,'Users/register.html',{'form':form})



@login_required
def Profile(request):
	if request.method == 'POST':
		u_form=UserUpdateForm(request.POST,instance=request.user)
		n_form=UserUpdateName(request.POST,instance=request.user.profile)
		#print(u_form)
		if  u_form.is_valid and n_form.is_valid:
			u_form.save()
			n_form.save()
			return redirect('Profile-page')
	else:
		u_form=UserUpdateForm(instance=request.user)
		n_form=UserUpdateName(instance=request.user.profile)

	context={'u_form':u_form,'n_form':n_form}	
	return render(request,'Users/profile.html',context)


class MyLoginView(LoginView):
    def get_success_url(self):
        return reverse('user-tasks', args=[self.request.user.username])