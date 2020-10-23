from django.contrib.auth.decorators import login_required
from .email import send_signup_email
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView