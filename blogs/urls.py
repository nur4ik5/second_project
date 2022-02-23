from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from profiles import views
from .views import *

urlpatterns = [
	path('blogs/', blog_list, name = 'blog_list'),
	path('comments/', comment_list, name = 'comment_list'),
	
]
