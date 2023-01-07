import praw
import time
import datetime

# creates reddit instance using credentials from praw.ini file
reddit = praw.Reddit("config")

# sets subreddit for bot to run in
subreddit_name = "a"
subreddit = reddit.subreddit(subreddit_name)

# will be populated with the usernames of the top 10 users each month
top_users = []

# will be populated with usernames and their participation score
user_rank = {}

# creates the template for the bot to send in its monthly message
message_template = ("Your top users list for r/%(subreddit_name)s from "
                    "%(month)s is ready. \n\n")

# prevents mods from being included in the top user list
excluded_users = list(subreddit.moderator())


t1 = time.time()
print(t1)

# https://www.reddit.com/r/redditdev/comments/7vj6ox/comment/dtszfzb/
# watches comment/submission streams and adds ids to respective lists
def monthly_activity():
    untallied_comments = []
    untallied_posts = []
    comment_stream = subreddit.stream.comments(pause_after=-1)
    submission_stream = subreddit.stream.submissions(pause_after=-1)
    while time.time() - t1 < 5: # will later replace this with logic that keeps loop running during the active month
        for comment in comment_stream:
            if comment is None:
                break
            untallied_comments.append(comment.id)
        for submission in submission_stream:
            if submission is None:
                break
            untallied_posts.append(submission.id)
    return untallied_comments, untallied_posts

print(monthly_activity())
print(time.time() - t1)



# sample user_rank for testing purposes; remove later
user_rank = {'a': 1, 'c': 3, 'd': 4, 'b': 2, 'f': 6, 'e': 5}

# sorts dict from highest value to lowest
user_rank = dict(sorted(user_rank.items(), key=lambda item: item[1], reverse=True))

# adds top 10 (or all if total users < 10) users to top_users
def top_users(user_rank):
    for user in user_rank:
        if len(top_users) < 10 and len(user_rank) != 0:
            if user in excluded_users:
                pass
            else:
                top_users.append(user)
        else:
            break
    return top_users

# placeholder; remove later
month = 'April'

# creates the final message that will be sent
message = message_template % {'subreddit_name': subreddit_name, 'month': month}


# sends message to mods for given month with given user rank
def message_send(month, user_rank):
    return


# goes through comments and posts and adds to user scores if the comments/posts are 12+ hours old
def tally(comment_list, submission_list):
    return


untallied_comments = []
untallied_posts = []

comment_stream = subreddit.stream.comments(pause_after=-1)
submission_stream = subreddit.stream.submissions(pause_after=-1)


while True:

    # if it's the active month or <= 12 hours into current month
    if (datetime.datetime.now() - datetime.timedelta(hours=12)).strftime("%B") != active_month:
        top_users()
        message_send()
        untallied_comments = []
        untallied_posts = []

    tally(untallied_comments, untallied_posts)

    for comment in comment_stream:
        if comment is None:
            break
        untallied_comments.append(comment.id)

    for submission in submission_stream:
        if submission is None:
            break
        untallied_posts.append(submission.id)