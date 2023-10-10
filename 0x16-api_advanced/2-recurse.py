#!/usr/bin/python3
"""
Query a subreddit without authentication
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """return list of all hot posts titles of a subreddit """
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {
        "User-agent": "Chrome/117.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            T = post['data']['title']
            hot_list.append(T)
        after = data['data']['after']
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None