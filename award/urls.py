from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('project/post/', views.post, name='post'),
    path('logout/', views.logout, name='logout'),
    path('user/profile/', views.profile, name='profile'),
    path('project/<int:project_id>/', views.project_detail, name='details'),
    path('search/projects/results/', views.search, name="search"),
    # path('ajax/review/<int:id>', views.ajaxRequest, name='review'),
    path('api/projects/', views.ProjectList.as_view(), name='api-projects'),
    path('api/profile/', views.ProfileList.as_view(), name='api-profile'),
    path('token/', obtain_auth_token, name='token'),
    path('developer/api/', views.apiView, name='api'),
    path('accounts/', include('django_registration.backends.activation.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
