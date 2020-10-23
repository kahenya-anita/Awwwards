from django.urls import path
from . import views

urlpatterns=[
    path('/',views.home,name = 'home'),
    path('email/',views.email,name = 'email'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('profile/(?P<profile_id>\d+)',views.profile,name = 'profile'),
]