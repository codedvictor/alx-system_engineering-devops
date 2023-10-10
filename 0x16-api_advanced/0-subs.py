#!/usr/bin/python3
"""  a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0"""

from requests import get


def number_of_subscribers(subreddit):
    """queries the Reddit and returns the number of subscribers"""
    if not isinstance(subreddit, str) or not subreddit:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-agent': 'Google Chrome Version 117.0.5938.132'}
    response = get(url, headers=user_agent)
    res = response.json()

    try:
        return res.get('data').get('subscribers')
    except Exception:
        return 0
