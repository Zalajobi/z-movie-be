def genreQueryString(key, genreId):
    return {"api_key": key, "language": "en-US", "sort_by": "popularity.desc", "include_adult": False,
            "include_video": False, "page": 1, "with_genres": genreId,
            "with_watch_monetization_types": "flatrate"}
