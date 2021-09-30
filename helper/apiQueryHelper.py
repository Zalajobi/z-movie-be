import requests


# Query API
def getRequest(url, param):
    return requests.request("GET", url, params=param)


def getMovieDetail(url, param):
    return requests.request("GET", url, params=param)
