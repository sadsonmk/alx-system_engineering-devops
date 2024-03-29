#!/usr/bin/python3
"""queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers)
    for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers

    args: subreddit

    return: number of subscribers or 0 if not valid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        return (data.get('subscribers'))
    else:
        return (0)
