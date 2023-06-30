from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from .models import Profile
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.urls import reverse_lazy


# Create your views here.

# Creation of the ProfileView class

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "users/profile.html"
    context_object_name = "profile"
    
    def get_object(self, queryset=None):
        return self.request.user
    
# Creation of view for updating the profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "users/profile_update.html"
    success_url = reverse_lazy("users:profile")
    
    def get_object(self, queryset=None):
        return self.request.user
    