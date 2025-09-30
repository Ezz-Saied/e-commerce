from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView, TemplateView
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

class SignUpView(View):
    def get(self,request):
        form = SignUpForm()
        return render(request, "accounts/signup.html", {"form": form})



    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, "accounts/signup.html", {"form": form})



class LoginView(View):
    def get(self, request):
        return render(request, "accounts/login.html",{})



    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect("home")
    



class ProfileView(TemplateView):
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "user"
