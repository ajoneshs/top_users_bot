import praw
import time

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

# watches comment/submission streams and adds ids to respective lists
def monthly_activity():
    monthly_comments = []
    monthly_posts = []
    comment_stream = subreddit.stream.comments(pause_after=-1)
    submission_stream = subreddit.stream.submissions(pause_after=-1)
    while time.time() - t1 < 5: # will later replace this with logic that keeps loop running during the active month
        for comment in comment_stream:
            if comment is None:
                break
            monthly_comments.append(comment.id)
        for submission in submission_stream:
            if submission is None:
                break
            monthly_posts.append(submission.id)
    return monthly_comments, monthly_posts

print(monthly_activity())
print(time.time() - t1)



# sample user_rank for testing purposes; remove later
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

# placeholder; remove later
month = 'April'

# creates the final message that will be sent
message = message_template % {'subreddit_name': subreddit_name, 'month': month}