from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login/', views.loginPage, name = 'login'),
    path('register/', views.registerPage, name = 'register'),
    path('accounts/logout/', views.logoutUser, name = 'logout'),
    path('',views.home,name = 'home'),
    path('email/',views.email,name = 'email'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('profile/<username>/',views.profile,name = 'profile'),
    path('project/<project_id>/',views.project,name = 'project'),
    path('add_project/',views.add_project,name = 'add_project'),
    path('rate_project/<project_id>/',views.rate_project,name = 'rate_project'),
    path('search_project/',views.search_project,name = 'search_project'),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profiles/', views.ProfileList.as_view()),
  
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)