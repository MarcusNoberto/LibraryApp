from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_form, name = 'home'),
    path('login/', views.loginView, name = 'login'),
    path('logout/', views.logoutView, name = 'logout'),
    path('regform/', views.register_form, name= 'regform'),
    path('register/', views.registerView, name='register'),



    #librarian urls
    path('librarian/', views.librarian, name='librarian'),
    path('labook_form/', views.labook_form, name='labook_form'),
    path('labook/', views.labook, name='labook'),
    path('llbook/', views.LBookListView.as_view(), name='llbook'),
    path('ldrequest/', views.LDeleteRequest.as_view(), name='ldrequest'),
    path('lsearch/', views.lsearch, name='lsearch'),
    path('ldbook/<int:pk>', views.LDeleteBook.as_view(), name='ldbook'),
    path('lmbook/', views.LManageBook.as_view(), name='lmbook'),
    path('ldbookk/<int:pk>', views.LDeleteView.as_view(), name='ldbookk'),
    path('lvbook/<int:pk>', views.LViewBook.as_view(), name='lvbook'),
    path('lebook/<int:pk>', views.LEditView.as_view(), name='lebook'),
    path('lcchat/', views.LCreateChat.as_view(), name='lcchat'),
    path('llchat/', views.LListChat.as_view(), name='llchat'),



    #admin urls
    path('administrador/', views.admin.as_view(), name = 'admin'),



    #publisher urls
    path('booklist/', views.BookList.as_view(), name = 'publisher'),
    path('uabook_form/', views.uabook_form, name='uabook_form'),
    path('uabook/', views.uabook, name='uabook'),
    path('ucchat', views.UserCreateChat.as_view(), name = 'ucchat'),
    path('ulchat/', views.UserListChat.as_view(), name='ulchat'),
    path('request_form/', views.request_form, name='request_form'),
    path('delete_request/', views.delete_request, name='delete_request'),
    path('feedback_form/', views.feedback_form, name='feedback_form'),
    path('send_feedback/', views.send_feedback, name='send_feedback'),
    path('about/', views.about, name='about'),
    path('usearch/', views.usearch, name='usearch'),
]

from django.conf import settings
from django.conf.urls.static import static

