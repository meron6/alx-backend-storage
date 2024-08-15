#!/usr/bin/env python3
"""
Create a web cache with expiration and access tracking.
"""
import redis
import requests

# Initialize the Redis client
rc = redis.Redis()

def get_page(url: str) -> str:
    """Fetch a page and cache the value with expiration."""
    # Check if the URL is already in cache
    cached_content = rc.get(f"cached:{url}")

    if cached_content:
        # Return cached content if available
        return cached_content.decode('utf-8')

    # Fetch the page from the URL if not in cache
    resp = requests.get(url)
    page_content = resp.text

    # Store the page content in cache with an expiration time of 10 seconds
    rc.setex(f"cached:{url}", 10, page_content)
    
    # Increment the access count
    rc.incr(f"count:{url}")

    return page_content

if __name__ == "__main__":
    url = 'http://slowwly.robertomurray.co.uk'
    page_content = get_page(url)
    print(page_content)
