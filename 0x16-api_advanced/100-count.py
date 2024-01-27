#!/usr/bin/python3
""" Recursive function that queries the Reddit API."""
import requests
import sys
after = None
count_dic = []


def count_words(subreddit, word_list):
    """Parse the title of all hot articles, and prints a sorted count of given.
    keywords (case-insensitive, delimited by spaces) """
    global after
    global count_dic
    headers = {'User-Agent': 'breasAPI'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)