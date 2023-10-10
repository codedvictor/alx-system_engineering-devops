#!/usr/bin/python3
""" a function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit"""

from requests import get


def top_ten(subreddit):
    """queries the top ten posts title"""
    if not isinstance(subreddit, str) or not subreddit:
        print("None")

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'limit': 10}
    user_agent = {'User-agent': 'Google Chrome Version 117.0.5938.132'}
    response = get(url, headers=user_agent, params=params)
    res = response.json()

    try:
        kids = res.get('data').get('children')
        for kid in kids:
            print(kid.get('data').get('title'))
    except Exception:
        print("None")
