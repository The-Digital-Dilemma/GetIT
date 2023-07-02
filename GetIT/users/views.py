from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm, CustomUserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.
# Custom LoginRequiredMixin to redirect unauthenticated users
class CustomLoginRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('users:login')

# Creation of the ProfileView class


class ProfileView(CustomLoginRequiredMixin, DetailView):
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

    # The post() method handles POST requests, validates the form data, saves the updated profile picture, and redirects to the profile page if the form is valid. Otherwise, it renders the form with the validation errors.

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES,
                           instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        context = {'form': form}
        return render(request, self.template_name, context)


# Creation of views for Login, Logout and Registration
class LoginInterfaceView(LoginView):
    template_name = 'users/login.html'
    next_page = 'courses_list'


class LogoutInterfaceView(LogoutView):
    template_name = 'users/logout.html'


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)
