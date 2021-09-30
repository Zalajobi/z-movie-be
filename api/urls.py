from django.urls import path
from . import views

urlpatterns = [
    path('topMovie', views.getTopMovies),
    path('trending/day', views.getTrendingAllDay),
    path('trending/week', views.getTrendingAllWeek),
    path('getItemInfo', views.getItemDetail),
    path('top-rated', views.getTopRated),
    path('latest-movie', views.getLatestMovies),
    path('upcoming', views.getLatestMovies),
]
