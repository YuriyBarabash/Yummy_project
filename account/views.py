from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy


def Logout_user(request):
    logout(request)
    return reverse('home:main_page')


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home:main_page')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = "register_user.html"
    success_url = 'home:main_page'

