from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Create your views here.

class SignUpView(CreateView):
		form_class = CustomUserCreationForm
		template_name = 'registration/signup.html'
		def get_success_url(self):
		    return reverse_lazy("home")