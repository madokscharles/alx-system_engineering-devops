#!/usr/bin/python3
"""
A recursive function that queries the Reddit API
Parses the title of all hot articles and prints a sorted
count of given keywords
"""
import re
from requests import get
import sys


def add_title(dictionary, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """Queries to Reddit API"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
                'User-Agent': '0x16-api_advanced:project:v1.0.0'
              }
    params = {
                'after': after
             }
    response = get(
                url, headers=headers, params=params,
                allow_redirects=False)

    if response.status_code != 200:
        return None

    dic = response.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ Init function """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    length = sorted(dictionary.items(), key=lambda kv: kv[1])
    length.reverse()

    if len(length) != 0:
        for item in length:
            if item[1] != 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
