from django.test import TestCase
from django.urls import path, include
from .views import SignUpView

# Create your tests here.

urlpatterns = [
	path('signup/',SignUpView.as_view(), name='signup'),
]