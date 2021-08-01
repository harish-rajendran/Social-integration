import sys
from slacker import Slacker


slack = Slacker(os.environ["SLACK_API_TOKEN"])
message = "Hello People!:tada:"
slack.chat.post_message('#general',message,as_user=False,username="Baby Walrus")
