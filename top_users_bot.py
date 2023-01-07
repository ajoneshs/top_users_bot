import praw
import time
import datetime


# **************Notes**************
# https://www.reddit.com/r/redditdev/comments/7vj6ox/comment/dtszfzb/
# **************End****************

# *@ = note on whether or not something works
# *$ = note on to-do


# creates reddit instance using credentials from praw.ini file
reddit = praw.Reddit("config")

# sets subreddit for bot to run in
subreddit_name = "a"
subreddit = reddit.subreddit(subreddit_name)

# creates the template for the bot to send in its monthly message
message_template = ("Your top users list for r/%(subreddit_name)s from "
                    "%(month)s is ready. \n\n")


# will be populated with usernames and their participation score
user_rank = {}

# sample user_rank for testing purposes; remove later
user_rank = {'a': 1, 'c': 3, 'd': 4, 'b': 2, 'f': 6, 'e': 5}


# adds top 10 (or all if total users < 10) users to top_users
# *@ works
def top_users(user_rank):
    top_users = []

    # prevents mods from being included in the top user list
    # included within function to update as moderators change
    excluded_users = list(subreddit.moderator())

    # sorts dict from highest value to lowest
    user_rank = dict(sorted(user_rank.items(), key=lambda item: item[1], reverse=True))

    for user in user_rank:
        if len(top_users) < 10 and len(user_rank) != 0:
            if user in excluded_users:
                pass
            else:
                top_users.append(user)
        else:
            break

    return top_users


# sends message to mods with current month's top_users
# currently just prints message instead of sending it
# *@ should work
def message_send(top_users):
    # might want to change message to have rank preceding username (i.e. 1: user1 \n 2: user2...)
    message = message_template % {'subreddit_name': subreddit_name, 'month': active_month} + '\n'.join(top_users)
    print(message)
    # add ability to send this message to mods


# goes through comments and posts and adds to user scores if the comments/posts are 12+ hours old
# *@ unfinished
# *$ write function
'''
def tally(untallied_comments, untallied_submissions):
    for counter, id in enumerate(untallied_comments):
        if 
'''


untallied_comments = []
untallied_submissions = []

comment_stream = subreddit.stream.comments(pause_after=-1)
submission_stream = subreddit.stream.submissions(pause_after=-1)

active_month = datetime.datetime.now().strftime("%B")



while True:

    # if it's the active month or <= 12 hours into current month
    if (datetime.datetime.now() - datetime.timedelta(hours=12)).strftime("%B") != active_month:
        # creates list of top 10 users
        local_top_users = top_users(user_rank)
        # sends message to mods with top 10 list
        message_send(local_top_users)
        # updates active month
        active_month = datetime.datetime.now().strftime("%B")

    # goes through currently untallied comments/submissions and, if it is at
    # at least 12 hours old, it calculates the participation score of the item
    # and updates user_rank
    # untallied_comments and untallied_submissions are updated to remove items
    # after they have been tallied
    # remove * after tally() has been finished
    # *$ finish tally() and remove # on line below
    # user_rank, untallied_comments, untallied_submissions = tally()

    for comment in comment_stream:
        if comment is None:
            break
        untallied_comments.append(comment.id)

    for submission in submission_stream:
        if submission is None:
            break
        untallied_submissions.append(submission.id)