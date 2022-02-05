from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from profiles import views
from profiles.views import *

urlpatterns = [
	path('', views.movie_list, name = 'movie_list'),
    path('me', views.my_profile, name = 'my_profile'),
    path('login_page', views.login_page, name = 'login_page'),
    path('logout_page', views.logout_page, name = 'logout_page'),

]







