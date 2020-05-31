
'''from slackclient import SlackClient
slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)
sc.api_call(
    "chat.postMessage",
    channel = "#python",
    text = "sassy brains - sent using PYTHON"
    )
curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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
'''


import sys
from slacker import Slacker
slack = Slacker("xoxb-1138370118131-1136878314997-blvcpMr9rKoGCaXHNQbuCiLx")
message = "Hello Everyone"
slack.chat.post_message('#general',message);