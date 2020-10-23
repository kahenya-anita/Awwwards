from django.contrib.auth.decorators import login_required
from .email import send_signup_email
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import CreateProfileForm

def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = CreateProfileForm()
    return render(request, 'user/create_profile.html', {"form": form, "title": title})

def email(request):
    current_user = request.user
    email = current_user.email
    name = current_user.username
    send_signup_email(name, email)
    return redirect(create_profile)