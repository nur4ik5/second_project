from django.shortcuts import render, redirect
from .models import Movie
from django .contrib.auth import authenticate, login, logout
from djengo.contrib.auth.decorators import login_required



def movie_list(request):
	movies = Movie.objects.all()
	context = {
		'movies': movies
	}
	return render(request, 'profiles/movie_list.html', context)


@login_required(login_url='/login_page')
def my_profile(request):
	""" Вьюха для просмотра Своего профиля """
	profile = request.user.profile
	context = {
		'profile': profile
	}
	return render(request, 'profiles/profile.html', context)

def login_page(request):
	""" Страница для входа """
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('my_profile')
	return render (request, 'profiles/login_page.html')


def logout_page(request):
	logout(user)
	return redirect('movie_list')




