import json
from django.http import JsonResponse
from helper.endpoints import key
from helper.apiQueryHelper import getRequest, getMovieDetail


# Create your views here.
def getTopMovies(request):
    if request.method == 'GET':
        pageNumber = 1
        queryString = {"api_key": key, "language": "en-US", 'page': pageNumber}
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/movie/popular', queryString).text))


def getTrendingAllDay(request):
    if request.method == 'GET':
        queryString = {"api_key": key}
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/trending/all/day', queryString).text))


def getTopRated(request):
    if request.method == "GET":
        queryString = {"api_key": key, 'language': 'en-US', 'page': 1}
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/movie/top_rated', queryString).text))


def getTrendingAllWeek(request):
    if request.method == 'GET':
        queryString = {"api_key": key}
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/trending/all/week', queryString).text))


def getLatestMovies(request):
    if request.method == "GET":
        queryString = {"api_key": key, "language": "en-US"}
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/movie/latest', queryString).text))


def getUpcomingMovies(request):
    if request.method == "GET":
        queryString = {"api_key": key, "language": "en-US"}
        return JsonResponse(json.loads(getRequest('https://api.themoviedb.org/3/movie/upcoming', queryString).text))


# POST REQUEST
# @csrf_exempt
def getItemDetail(request):
    if request.method == 'POST':
        queryString = {"api_key": key, "language": "en-US"}
        movieId = json.loads(request.body.decode('utf-8'))
        return JsonResponse(json.loads(
            getMovieDetail('https://api.themoviedb.org/3/movie/' + str(movieId['movieId']), queryString).text))


def getSimilarMovie(request):
    if request.method == "POST":
        params = json.loads(request.body.decode('utf-8'))
        queryString = {"api_key": key, "language": "en-US", "page": 1}
        # print(getRequest('https://api.themoviedb.org/3/movie/' + params['id'] + '/similar', queryString).text)
        return JsonResponse(json.loads(
            getMovieDetail('https://api.themoviedb.org/3/movie/' + str(params['id']) + '/similar', queryString).text))


# def getThriller(request):
#     return None