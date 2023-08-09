#!/usr/bin/python3
"""
Function queries the Reddit API,
Returns the number of sunscribers (not active users, total subs)
"""

from requests import get


def number_of_subscribers(subreddit):
    """Total number of subs for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    response = get(
        'http://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={'User-Agent': '0x16-api_advanced:project:\
                        v1.0.0'}).json()
    subs = response.get("data", {}).get("subscribers", 0)
    return subs
