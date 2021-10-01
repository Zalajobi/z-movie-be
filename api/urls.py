from django.urls import path
from . import views

urlpatterns = [
    path('topMovie', views.getTopMovies),
    path('trending/day', views.getTrendingAllDay),
    path('trending/week', views.getTrendingAllWeek),
    path('getMovieInfo', views.getItemDetail),
    path('top-rated', views.getTopRated),
    path('latest-movie', views.getLatestMovies),
    path('upcoming', views.getLatestMovies),
    path('similar-movie', views.getSimilarMovie),
    # path('movie/thriller', views.getThriller)
]
