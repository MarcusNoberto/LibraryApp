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
from .forms import ChatForm
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

def uabook_form(request):
	return render(request, 'publisher/add_book.html')

class BookList(ListView):
	model = models.Book
	template_name = 'publisher/book_list.html'
	context_object_name = 'books'
	paginate_by = 4

	def get_queryset(self):
		return models.Book.objects.order_by('-id')

@login_required
def uabook(request):
	if request.method == 'POST':
		title = request.POST['title']
		author = request.POST['author']
		year = request.POST['year']
		publisher = request.POST['publisher']
		desc = request.POST['desc']
		cover = request.POST.get('cover', False)
		pdf = request.POST.get('pdf', False)
		current_user = request.user
		user_id = current_user.id
		username = current_user.username

		a = models.Book(title=title, author=author, year=year, publisher=publisher,
			desc=desc, cover=cover, pdf=pdf, uploaded_by=username, user_id=user_id)
		a.save()
		messages.success(request, 'Book was uploaded successfully')
		return redirect('publisher')
	else:
		messages.error(request, 'Book was not uploaded successfully')
		return redirect('uabook_form')

class UserCreateChat(LoginRequiredMixin, CreateView):
	form_class = ChatForm
	model = models.Chat
	template_name = 'publisher/chat_form.html'
	success_url = reverse_lazy('ulchat')

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)

class UserListChat(LoginRequiredMixin, ListView):
	model = models.Chat
	template_name = 'publisher/chat_list.html'

	def get_queryset(self):
		return models.Chat.objects.filter(posted_at__lt=timezone.now()).order_by('posted_at')

@login_required
def request_form(request):
	return render(request, 'publisher/delete_request.html')

@login_required
def delete_request(request):
	if request.method == 'POST':
		book_id = request.POST['delete_request']
		current_user = request.user
		user_id = current_user.id
		username = current_user.username
		user_request = username + "  want book with id  " + book_id + " to be deleted"

		a = models.DeleteRequest(delete_request=user_request)
		a.save()
		messages.success(request, 'Request was sent')
		return redirect('publisher')
	else:
		messages.error(request, 'Request was not sent')
		return redirect('request_form')





#Librariam views
class librarian(TemplateView):
	template_name = 'librarian/home.html'



