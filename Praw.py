import praw
reddit=praw.Reddit(client_id='s9inVPVxGJdV3Q',
                   client_secret='N-iQ0ReWYTa2EoQxAzkqqL4fQU8',
                   user_agent='wtfisthis')

user1=input("Enter First User ")
user2=input("Enter Second User ")

for submission in reddit.redditor(user1).submissions.new(limit=1):
    ups1=submission.score

for submission in reddit.redditor(user2).submissions.new(limit=1):
    ups2=submission.score

if ups1>ups2:
	print(user1,"got more up votes")
else:
	print(user2,"got more up votes")
