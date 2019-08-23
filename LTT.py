import praw

import config

import time

import os

from random import randrange

import re



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

    





def run_bot(r, comments_replied_to, get_random_line, WholeWord):



    



    for comment in r.subreddit('TobussTest').comments(limit=10):

        commentb = comment.body

        

        with open('./Responses/LTTResponses.txt', "r" ,encoding='utf-8') as LTTResponses:

            for line in LTTResponses:

                line = line.rstrip()

                if WholeWord(line)(comment.body) and comment.id not in comments_replied_to and comment.author != r.user.me():

                    print("String found in comment" + " " + comment.id)

                    with open('lews.txt', encoding='utf-8') as f:

                        comment.reply(get_random_line(f))

                    



                    print("replied to comment" + " " + comment.id)



                    comments_replied_to.append(comment.id)

                    



                    with open("comments_replied_to.txt", "a") as f:

                        f.write(comment.id + "\n")



        with open('./Responses/AResponses.txt', "r" ,encoding='utf-8') as AResponses:

            for Aline in AResponses:

                Aline = Aline.rstrip()          

                if WholeWord(Aline)(commentb) and comment.id not in comments_replied_to and comment.author != r.user.me():



                    print("String found in comment" + " " + comment.id)

                    with open('ashaman.txt', encoding='utf-8') as f:

                        comment.reply(get_random_line(f))



                    print("replied to comment" + " " + comment.id)



                    comments_replied_to.append(comment.id)

                    



                    with open("comments_replied_to.txt", "a") as f:

                        f.write(comment.id + "\n")

        

        with open('./Responses/WResponses.txt', "r" ,encoding='utf-8') as WResponses:

            for Wline in WResponses:

                Wline = Wline.rstrip()          

                if WholeWord(Wline)(commentb) and comment.id not in comments_replied_to and comment.author != r.user.me():

                    print("String found in comment" + comment.id)

                    with open('women.txt', encoding='utf-8') as f:

                        comment.reply(get_random_line(f))



                    print("replied to comment" + " " + comment.id)



                    comments_replied_to.append(comment.id)

                    



                    with open("comments_replied_to.txt", "a") as f:

                        f.write(comment.id + "\n")



        with open('./Responses/BWResponses.txt', "r" ,encoding='utf-8') as BWResponses:

            for BWline in BWResponses:

                BWline = BWline.strip()          

                if WholeWord(BWline)(commentb) and comment.id not in comments_replied_to and comment.author != r.user.me():

                    print("String found in comment" + comment.id)

                    with open('bwoman.txt', encoding='utf-8') as f:

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