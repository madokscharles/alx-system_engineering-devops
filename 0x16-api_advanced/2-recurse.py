#!/usr/bin/python3
"""
Function queries the Reddit API
Returns a list containing the titles of all hot articles for a subreddit
"""

from requests import get
after = None


def recurse(subreddit, hot_list=[]):
    """Returning top ten post titles"""
    global after

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {
                'User-Agent': '0x16-api_advanced:project:v1.0.0'
              }
    params = {
                "after": after
             }
    response = get(
                url, headers=headers, params=params,
                allow_redirects=False)

    if response.status_code == 200:
        after_data = response.json().get('data').get('after')
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)

        c_titles = response.json().get("data").get("children")
        for c in c_titles:
            hot_list.append(c.get("data").get("title"))
        return hot_list
    else:
        return None
