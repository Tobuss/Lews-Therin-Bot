import json
import os
import random
import re
import praw
import config

KEYWORDS = json.load(open('keywords.json', 'r'))
QUOTES = json.load(open('quotes.json', 'r'))
CATEGORIES = ['lews', 'woman', 'bwoman', 'ashaman']


def bot_login():
    return praw.Reddit(username=config.username,
                       password=config.password,
                       client_id=config.client_id,
                       client_secret=config.client_secret,
                       user_agent="Lews Therin WoT Bot to scream nonsense")


def comment_has_keyword(keywords, comment_body):
    for keyword in keywords:
        pattern = re.compile(r'\b({0})\b'.format(keyword), flags=re.IGNORECASE)
        if pattern.search(comment_body):
            # found a match, no reason to continue checking keywords
            return True
    return False


def run_bot(reddit, comments_replied_to):
    for comment in reddit.subreddit('TobussTest').comments(limit=10):
        if comment.author == reddit.user.me() or comment.id in comments_replied_to:
            # Either this comment was made by the bot, or we've already responded to it.
            continue

        for category in CATEGORIES:
            if comment_has_keyword(KEYWORDS[category], comment.body):
                print("String found in comment " + comment.id)
                respond_to_comment(comment, QUOTES[category], comments_replied_to)
                # Comment has been made, no reason to continue checking other matches
                break


def respond_to_comment(comment, quotes, comments_replied_to):
    quote = random.choice(quotes)
    comment.reply(quote)
    print("replied to comment " + comment.id)
    comments_replied_to.append(comment.id)
    with open("comments_replied_to.txt", "a") as f:
        f.write(comment.id + "\n")


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
    return comments_replied_to


def run():
    reddit = bot_login()
    comments_replied_to = get_saved_comments()
    while True:
        run_bot(reddit, comments_replied_to)
