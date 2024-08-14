import os
import pickle
CACHE_LOCATION = "cache"

def cache_query(query):
    """
    Check if the query is cached and return the result if it is.
    """
    cache_file = os.path.join(CACHE_LOCATION, f"{query}.pkl")
    if os.path.exists(cache_file):
        with open(cache_file, "rb") as f:
            return pickle.load(f)
    return None

def cache_result(query, result):
    """
    Cache the result of the query.
    """
    cache_file = os.path.join(CACHE_LOCATION, f"{query}.pkl")
    with open(cache_file, "wb") as f:
        pickle.dump(result, f)


def clear_cache():
    """
    Clear the cache directory.
    """
    for file in os.listdir(CACHE_LOCATION):
        os.remove(os.path.join(CACHE_LOCATION, file))

