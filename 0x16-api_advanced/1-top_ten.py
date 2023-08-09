#!/usr/bin/python3
"""
Function queries the Reddit API
Prints the titles of the first 10 hot posts listed
"""

from requests import get


def top_ten(subreddit):
    """Prints the titles of the first 10 host posts listed"""
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {
                'User-Agent': '0x16-api_advanced:project:v1.0.0'
              }
    params = {
                "limit": 10
             }
    response = get(
                url, headers=headers, params=params,
                allow_redirects=False)

    if response.status_code == 404:
        print('None')
        return

    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
