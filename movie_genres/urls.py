from django.urls import path
from . import views

urlpatterns = [
    path('action', views.getActionMovies),
    path('adventure', views.getAdventureMovies),
    path('animation', views.getAnimationMovies),
    path('comedy', views.getComedyMovies),
    path('crime', views.getCrimeMovies),
    path('documentary', views.getDocumentaryMovies),
    path('drama', views.getDramaMovies),
    path('family', views.getFamilyMovies),
path('fantasy', views.getFantasyMovies),
path('history', views.getHistoryMovies),
path('horror', views.getHorrorMovies),
path('music', views.getMusicMovies),
path('mystery', views.getMysteryMovies),
path('romance', views.getRomanceMovies),
path('science-fiction', views.getScienceFictionMovies),
path('tv-movies', views.getTvMoviesMovies),
path('thriller', views.getThrillerMovies),
path('war', views.getWarMovies),
path('western', views.getWesternMovies),
]
