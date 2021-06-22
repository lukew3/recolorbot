import praw
import requests
import json

r = praw.Reddit()

API_KEY = open("api-key.txt", "r").read().strip()

def make_response(message):
    print("Processing request...")
    submission = message.submission
    if submission.is_self:
        # Submission is not a link post
        return "Image not found"
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        data={'image': submission.url},
        headers={'api-key': API_KEY}
    )
    try:
        if (r.json())["err"]:
            # Error during colorization
            return "An error occurred during colorization. Original post must be an image or a direct link to an image. You can still generate a colorized image by downloading and uploading manually to [DeepAI Image Colorizer](https://deepai.org/machine-learning-model/colorizer)"
    except Exception:
        new_image_url = (r.json())["output_url"]
        return f"[Colorized image]({new_image_url})"

footer = "\n\n ^( [dev](https://github.com/lukew3/)|[source](https://github.com/lukew3/recolorbot) )" 
messages = r.inbox.stream()
print("Awaiting requests")
for message in messages:
    try:
        if message in r.inbox.mentions() and message in r.inbox.unread():
            message.reply(make_response(message) + footer)
            message.mark_read()
            print("Message sent")
    except praw.exceptions.APIException:
        print("Probably hit rate limit")

