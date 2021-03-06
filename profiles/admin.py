from django.contrib import admin
from .models import Movie, MovieImage, Profile, Category

class MovieImageInLine(admin.TabularInline):
	model = MovieImage


class MovieAdmin(admin.ModelAdmin):
	inlines = [MovieImageInLine]


admin.site.register(Movie, MovieAdmin)
# admin.site.register(MovieImage)
admin.site.register(Profile)
admin.site.register(Category)