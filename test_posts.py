import praw
import time

reddit_list = [praw.Reddit("test1"), praw.Reddit("test2"), praw.Reddit("test3")]
start_time = time.time()
scores = [0, 0, 0]
subreddit_name = "ajoneshsbottest"
counter = 0
submission_ids = []

try:
    while time.time() - start_time < 36000:
        counter += 1
        for i in reddit_list:
            reddit = i
            title = str(reddit.user.me()) + "\'s post number " + str(counter)
            submission_ids.append(reddit.subreddit(subreddit_name).submit(title, selftext='test'))
            print('created post with title: ' + title)
            # will later add scoring here
            time.sleep(120)

except Exception as exception:
    print(exception)
    print(submission_ids)
 

# print(scores)