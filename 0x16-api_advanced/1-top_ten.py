#!/usr/bin/python3
"""
Query a subreddit without authentication
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-agent": "Chrome/117.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            T = post['data']['title']
            print(T)
    else:
        print('None')
