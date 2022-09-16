import praw

import config

import time

import os

from random import randrange

import re

import prawcore

from prawcore import PrawcoreException

from requests.exceptions import ConnectionError, HTTPError, Timeout

def failable(f):
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except praw.exceptions.APIException:
            full = traceback.format_exc()
            logging.warning("Reddit API call failed! %s" % full)
            return None
        except ConnectionError:
            full = traceback.format_exc()
            logging.warning("Connection error: %s", full)
        except HTTPError:
            full = traceback.format_exc()
            logging.warning("HTTP error %s" % full)
            return None
    return wrapped

def bot_login():

    r = praw.Reddit(username = config.username,

            password = config.password,

            client_id = config.client_id,

            client_secret = config.client_secret,

            user_agent = "Lews Therin WoT Bot to scream nonsense")

    return r



  



def get_random_line(afile, default=None):

    """Return a random line from the file (or default)."""

    line = default

    for i, aline in enumerate(afile, start=1):

        if randrange(i) == 0:  # random int [0..i)

            line = aline

    return line



#used for finding the whole word, wanted to avoid using RegEx

def WholeWord(w):

    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

    




@failable
def run_bot(r, comments_replied_to, get_random_line, WholeWord):



    



    for comment in r.subreddit('WetlanderHumor').comments(limit=10):

        commentb = comment.body

        with open('C:\LTTBot\\banned.txt', "r" ,encoding='utf-8') as banned:
            for bword in banned:
                bword = bword.strip()

                if WholeWord(bword)(commentb) and comment.id not in comments_replied_to and comment.author != r.user.me():
                    print("Comment contains banned word" + " " + comment.id)
                    comments_replied_to.append(comment.id)

       

        with open('C:\LTTBot\Responses\LTTResponses.txt', "r" ,encoding='utf-8') as LTTResponses:

            for line in LTTResponses:

                line = line.rstrip()

                if WholeWord(line)(comment.body) and comment.id not in comments_replied_to and comment.author != r.user.me():

                    print("String found in comment" + " " + comment.id)

                    with open('C:\LTTBot\lews.txt', encoding='utf-8') as f:

                        comment.reply(get_random_line(f))

                    



                    print("replied to comment" + " " + comment.id)



                    comments_replied_to.append(comment.id)

                    



                    with open("comments_replied_to.txt", "a") as f:

                        f.write(comment.id + "\n")



        with open('C:\LTTBot\Responses\\AResponses.txt', "r" ,encoding='utf-8') as AResponses:

            for Aline in AResponses:

                Aline = Aline.rstrip()          

                if WholeWord(Aline)(commentb) and comment.id not in comments_replied_to and comment.author != r.user.me():



                    print("String found in comment" + " " + comment.id)

                    with open('C:\LTTBot\\ashaman.txt', encoding='utf-8') as f:

                        comment.reply(get_random_line(f))



                    print("replied to comment" + " " + comment.id)



                    comments_replied_to.append(comment.id)

                    



                    with open("comments_replied_to.txt", "a") as f:

                        f.write(comment.id + "\n")

        

        with open('C:\LTTBot\Responses\WResponses.txt', "r" ,encoding='utf-8') as WResponses:

            for Wline in WResponses:

                Wline = Wline.rstrip()          

                if WholeWord(Wline)(commentb) and comment.id not in comments_replied_to and comment.author != r.user.me():

                    print("String found in comment" + comment.id)

                    with open('C:\LTTBot\women.txt', encoding='utf-8') as f:

                        comment.reply(get_random_line(f))



                    print("replied to comment" + " " + comment.id)



                    comments_replied_to.append(comment.id)

                    



                    with open("comments_replied_to.txt", "a") as f:

                        f.write(comment.id + "\n")



        with open('C:\LTTBot\Responses\BWResponses.txt', "r" ,encoding='utf-8') as BWResponses:
            for BWline in BWResponses:

                BWline = BWline.strip()          


                if WholeWord(BWline)(commentb) and comment.id not in comments_replied_to and comment.author != r.user.me():

                    print("String found in comment" + comment.id)

                    with open('C:\LTTBot\\bwoman.txt', encoding='utf-8') as f:

                        comment.reply(get_random_line(f))



                    print("replied to comment" + " " + comment.id)



                    comments_replied_to.append(comment.id)

                    



                    with open("comments_replied_to.txt", "a") as f:

                        f.write(comment.id + "\n")

    

        # print("Sleeping for 10 seconds...")

        #time.sleep(10)



def randomlink():

    return random.choice(lines)









def get_saved_comments():

    if not os.path.isfile("comments_replied_to.txt"):

        comments_replied_to = []

    else:

        with open("comments_replied_to.txt", "r") as f:

            comments_replied_to = f.read()

            comments_replied_to = comments_replied_to.split("\n")

            #comments_replied_to = filter(None, comments_replied_to)



    return comments_replied_to



r = bot_login()

comments_replied_to = get_saved_comments()



while True:

    run_bot(r, comments_replied_to, get_random_line, WholeWord)