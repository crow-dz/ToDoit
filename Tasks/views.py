from django.shortcuts import render , get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . models import tasks
#**********************************
from django.views.generic import ListView , CreateView , UpdateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
#**********************************
from django.contrib.auth.models import User
from django.urls import reverse_lazy


def index(request):
	return render(request,'Tasks/index.html')

class TaskListView(ListView):
	model =  tasks
	template_name = 'Tasks/base.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'all_tasks'
	paginate_by = 5
	ordering=['completed']
	

class TaskCreateView(LoginRequiredMixin,CreateView):
	model = tasks
	fields=['task','priority']
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class TaskUpadteView(LoginRequiredMixin,UpdateView):
	model=tasks
	template_name = 'Tasks/tasks_update.html'
	fields=['task','priority','completed']
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)
	

class UserTaskListView(ListView):
	model = tasks
	template_name ='Tasks/user_tasks.html'
	context_object_name='user_tasks'
	def get_queryset(self):
		user=get_object_or_404(User , username=self.kwargs.get('username'))
		return tasks.objects.filter(author=user).order_by('completed')
	paginate_by = 5





class UserDeleteView(LoginRequiredMixin,DeleteView):
	model=tasks
	def get_success_url(self):         
		return reverse_lazy('user-tasks', kwargs={'username': self.request.user.username})
	def test_func(self):
		task=self.get_object()
		if self.request.user == task.user:
			return True
		return False


