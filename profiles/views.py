from django.shortcuts import render
from .models import Movie

def movie_list(request):
	movies = Movie.objects.all()
	context = {
		'movies': movies
	}
	return render(request, 'profiles/movie_list.html', context)