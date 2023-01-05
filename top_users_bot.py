import praw

# creates reddit instance using credentials from praw.ini file
reddit = praw.Reddit("config")

# sets subreddit for bot to run in
subreddit_name = "name"
subreddit = reddit.subreddit(subreddit_name)


# creates the template for the bot to send in its monthly message
message_template = """Your top users list for r/%(subreddit_name)s from 
                      %(month)s is ready. \n\n"""

# prevents mods from being included in the top user list
excluded_users = list(subreddit.moderator())