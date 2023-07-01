from django.shortcuts import render, redirect
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
    
    # The get() method handles GET requests and renders the form with the existing profile picture.
    
    def get(self, request):
        form = ProfileForm(instance=request.user.profile)
        context = {'form': form}
        return render(request, self.template_name, context)
    
    #The post() method handles POST requests, validates the form data, saves the updated profile picture, and redirects to the profile page if the form is valid. Otherwise, it renders the form with the validation errors.
    
    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        context = {'form': form}
        return render(request, self.template_name, context)
    
    

    
    