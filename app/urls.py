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
    path('librarian/', views.librarian.as_view(), name = 'librarian' ),



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
]

from django.conf import settings
from django.conf.urls.static import static

