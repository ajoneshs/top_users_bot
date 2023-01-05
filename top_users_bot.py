import praw
import time

# creates reddit instance using credentials from praw.ini file
reddit = praw.Reddit("config")

# sets subreddit for bot to run in
subreddit_name = "progressivedemocrats"
subreddit = reddit.subreddit(subreddit_name)

# will be populated with the usernames of the top 10 users each month
top_users = []

# will be populated with usernames and their participation score
user_rank = {}


# creates the template for the bot to send in its monthly message
message_template = """Your top users list for r/%(subreddit_name)s from 
                      %(month)s is ready. \n\n"""

# prevents mods from being included in the top user list
excluded_users = list(subreddit.moderator())


'''
for comment in subreddit.stream.comments():
    print(comment)
    print('hello')

for submission in subreddit.stream.submissions():
    print(submission)
    print('yo')
'''

# sample user_rank for testing purposes
user_rank = {'a': 1, 'c': 3, 'd': 4, 'b': 2, 'f': 6, 'e': 5}

# sorts dict from highest value to lowest
user_rank = dict(sorted(user_rank.items(), key=lambda item: item[1], reverse=True))

# adds top 10 (or all if total users < 10) users to top_users
for user in user_rank:
    if len(top_users) < 10 and len(user_rank) != 0:
        if user in excluded_users:
            pass
        else:
            top_users.append(user)
    else:
        break
