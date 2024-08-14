"""
This module provides a simple caching system to store the results of queries.
The cache_query function checks if a query is cached and returns the result if it is.
The cache_result function caches the result of a query.

Functions:
- cache_query: Check if the query is cached and return the result if it is.
- cache_result: Cache the result of the query.
- clear_cache: Clear the cache directory.

Usage:
The cache_query function can be used to check if a query result is cached.
The cache_result function can be used to cache the result of a query.
The clear_cache function can be used to clear the cache directory.

Example:
result = cache_query("test_query")
if result is None:
    result = perform_query("test_query")
    cache_result("test_query", result)
print(result)
"""

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
