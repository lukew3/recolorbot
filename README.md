# Recolor Bot 

A Reddit bot that colorizes a black and white image post on reddit. When the bot is tagged, it grabs the image url from the reddit post and sends it to [The DeepAI Image Colorization API](https://deepai.org/machine-learning-model/colorizer).

## Setup
1. Create a `praw.ini` file with all of the necessary fields (client_id, client_secret, password, and username). [Documentation here](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html)
2. Create the file `api-key.txt` and paste your deepai key inside of the file
3. Install praw with `pip install praw`
4. Run with `python main.py`
