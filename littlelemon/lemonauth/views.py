from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView ,LogoutView
from .forms import SignupForm ,LoginForm
from django.views.generic import FormView ,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts  import redirect
from django.contrib import messages


class SignupView (FormView):
    form_class= SignupForm
    template_name ='lemonauth/signup.html'
    success_url =reverse_lazy('login')

    def form_valid(self,form):
        print("Form valid and will be saved.")
        form.save()
        messages.success(self.request, "Account created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form invalid")
        print(form.errors) 
        messages.error(self.request,"the form is invalid there's error in your submission ")
        return super().form_invalid(form)


class HomeView(TemplateView):
    template_name = 'home.html'


class LogunView (LoginView):
    form_class= LoginForm
    template_name = 'lemonauth/signin.html'
    success_url = reverse_lazy('home') 
    def form_valid(self,form):
        user= form.get_user()
        if not user.is_loggedin:
            user.is_loggedin = True
            user.save()
        return super().form_valid(form)

    
User = get_user_model()
class CustomLogoutViews(LogoutView):
    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_authenticated:
            user= request.user
            user.is_loggedin = False
            user.save()
        response = super().dispatch(request, *args, **kwargs)
        return redirect('login')
