import json
from django.http import JsonResponse
from helper.endpoints import key
from helper.apiQueryHelper import getRequest, getMovieDetail
from helper.constants import genreQueryString

genreId = "set genre id"


# Create your views here.
def getActionMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 28)).text))


def getAdventureMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 12)).text))


def getAnimationMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 16)).text))


def getComedyMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 35)).text))


def getCrimeMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 80)).text))


def getDocumentaryMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 99)).text))


def getDramaMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 18)).text))


def getFamilyMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 10751)).text))


def getFantasyMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 14)).text))


def getHistoryMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 36)).text))


def getHorrorMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 27)).text))


def getMusicMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 10402)).text))


def getMysteryMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 9648)).text))


def getRomanceMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 10749)).text))


def getScienceFictionMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 878)).text))


def getTvMoviesMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 10770)).text))


def getThrillerMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 53)).text))


def getWarMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 10752)).text))


def getWesternMovies(request):
    if request.method == 'GET':
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/discover/movie', genreQueryString(key, 37)).text))