import praw

reddit_list = [praw.Reddit("test1"), praw.Reddit("test2"), praw.Reddit("test3")]

for i in reddit_list:
    reddit = i
    for submission in reddit.user.me().submissions.new():
        submission.delete()
        print(str(submission) + ' was deleted')
    for comment in reddit.user.me().comments.new():
        comment.delete()
        print(str(comment) + ' was deleted')