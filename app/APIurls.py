from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import APIviews

router = DefaultRouter()
router.register(r'books', APIviews.BookViewSet,basename="book")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]