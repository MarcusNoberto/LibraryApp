from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.contrib import messages
from django.db.models import Sum
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView, TemplateView
from . import models
import operator
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, logout
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def login_form(request):
	return render(request, 'login.html')

def logoutView(request):
	logout(request)
	return redirect('home')

def register_form(request):
	return render(request, 'register.html')

def registerView(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password = make_password(password)

		a = models.User(username=username, email=email, password=password)
		a.save()
		messages.success(request, 'Account was created successfully')
		return redirect('home')
	else:
		messages.error(request, 'Registration fail, try again later')
		return redirect('regform')



def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			if user.is_superuser:
				return redirect('admin')
			elif user.is_librarian:
				return redirect('librarian')
			else:
				return redirect('publisher')
		else:
			messages.info(request, "Invalid username or password")
			return redirect('home')


#Admin views
class admin(TemplateView):
	template_name = 'admin/home.html'

#Publisher views
class publisher(TemplateView):
	template_name = 'publisher/publisher_home.html'

class BookList(ListView):
	model = models.Book
	template_name = 'publisher/book_list.html'
	context_object_name = 'books'
	paginate_by = 4

	def get_queryset(self):
		return models.Book.objects.order_by('-id')



#Librariam views
class librarian(TemplateView):
	template_name = 'librarian/home.html'



