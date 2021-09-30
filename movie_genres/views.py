import json
from django.http import JsonResponse
from helper.endpoints import key
from helper.apiQueryHelper import getRequest, getMovieDetail


# Create your views here.
def getActionMovies(request):
    if request.method == 'GET':
        queryString = {"api_key": key, "language": "en-US", "sort_by": "popularity.desc", "include_adult": False,
                       "include_video": False, "page": 1, "with_genres": 28,
                       "with_watch_monetization_types": "flatrate"}
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', queryString).text))


def getComedyMovies(request):
    if request.method == 'GET':
        queryString = {"api_key": key, "language": "en-US", "sort_by": "popularity.desc", "include_adult": False,
                       "include_video": False, "page": 1, "with_genres": 35,
                       "with_watch_monetization_types": "flatrate"}
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', queryString).text))
