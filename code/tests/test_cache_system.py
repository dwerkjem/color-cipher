"""
Test the cache system.

Functions:

- test_cache_systems: Test the retrieval of a cached query.
- test_cache_systems_no_cache: Test the retrieval of a non-cached query.
- test_cache_systems_clear_cache: Test the clearing of the cache.

Modules:

- cache_system: Contains functions for caching query results.

Usage:

To run the tests, run `pytest code/tests/test_cache_system.py` from the root directory.
"""

from code.src.cache_system import cache_query, cache_result, clear_cache


def test_cache_systems():
    """
    Test the retrieval of a cached query.
    """
    mock_query = "test_query"
    mock_result = "test_result"
    cache_result(mock_query, mock_result)
    result = cache_query(mock_query)
    assert result == mock_result, f"Expected {mock_result}, but got {result}"


def test_cache_systems_no_cache():
    """
    Test the retrieval of a non-cached query.
    """
    mock_query = "test_query2"
    result = cache_query(mock_query)
    assert result is None, f"Expected None, but got {result}"


def test_cache_systems_clear_cache():
    """
    Test the clearing of the cache.
    """
    mock_query = "test_query3"
    mock_result = "test_result3"
    cache_result(mock_query, mock_result)
    result_pre_clear = cache_query(mock_query)
    assert (
        result_pre_clear == mock_result
    ), f"Expected {mock_result}, but got {result_pre_clear}"
    clear_cache()
    result = cache_query(mock_query)
    assert result is None, f"Expected None, but got {result}"
