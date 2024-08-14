#!/usr/bin/env python3
import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()

def cache_with_count(fn: Callable) -> Callable:
    """Decorator to cache the result of a function and count accesses."""

    @wraps(fn)
    def wrapper(url: str) -> str:
        # Track the access count for the URL
        r.incr(f"count:{url}")

        # Check if the URL content is already cached
        cached_page = r.get(f"cached:{url}")
        if cached_page:
            return cached_page.decode("utf-8")

        # If not cached, get the page content and cache it
        content = fn(url)
        r.setex(f"cached:{url}", 10, content)
        return content

    return wrapper

@cache_with_count
def get_page(url: str) -> str:
    """Fetch the HTML content of a URL."""
    response = requests.get(url)
    return response.text
