# top_users_bot

Please note, this bot is not currently finished. The instructions below will only apply when the bot is finished and ready to be used.


## About
This bot will send the moderators of a subreddit a list of the top 10 contributors each month.

## Setup

### Obtain a set of credentials

This is done to allow you to interact with the Reddit API.
You will need a Reddit account if you do not already have one.
To obtain the necessary credentials, Reddit has created a guide which you can find [here](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps_). 
The guide is a little unclear about where you can find your client ID—it is the alphanumeric string you will find under the text "personal use script" after you have clicked the "create app" button. 
 
### Create a config file

You can do this with any text editor, i.e. Notepad on Windows. Open a text editor and paste the below text.

```
[config]
client_id=replace
client_secret=replace
password=replace
username=replace
user_agent=bot run by u/your_username_here
```
Replace each section where the word ```replace``` appears with your own credentials and add your username to the user agent.
Save this file as ```praw.ini``` and make sure it is saved in the same folder as this bot.

### Run the bot

Run the bot by opening the ```top_users_bot.py``` file.
Everything else will happen automatically; you just have to let the script run.
To ensure everything is working properly, you will receive a starting message to let you know the bot is running.
After that, you will receive a message on the first of each month with a list of the top 10 users of your subreddit.
