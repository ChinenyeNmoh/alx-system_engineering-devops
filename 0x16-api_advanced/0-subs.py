#!/usr/bin/python3
"""
query a subreddit without authentification
"""
import requests


def number_of_subscribers(subreddit):
	"""
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
	url = f"https://www.reddit.com/r/{subreddit}/about.json"
	headers = {"User-agent": "Chrome/117.0.0.0 Safari/537.36"}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		data = response.json()
		return (data['data']['subscribers'])
	else:
		return (0)