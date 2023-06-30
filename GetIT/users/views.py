from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.

# Creation of the ProfileView class

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "users/profile.html"
    context_object_name = "profile"
    
    def get_object(self, queryset=None):
        return self.request.user
    
    

