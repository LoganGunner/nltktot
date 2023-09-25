import nltk
import re
from nltk.text import Text
import sys


###################################[ Constants ]######################################

USERNAMEEXPRESSION = "<[A-Za-z0-9]+>" # RegEx for usernames contained between <>
SYSTEMUSERNAME = "-!-" # The tag for system messages, change based on system/chat log origins
TIMESTAMPEXPRESSION = "\[[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?\]" # RegEx for timestamp as [HH:MM:SS.MS]
KEYWORDS = [ # List of Keywords to reference
    'torchlight2', 'tl2'
]

######################################################################################

# file = open('IRCsamplechat.txt')

# text = open('chatmessages.txt', "w")

# for line in file.readlines():
#    # line = line.strip("\n")
#     timestamp = re.search(TIMESTAMPEXPRESSION, line).group()
#     username = re.search(USERNAMEEXPRESSION, line)
#     if not username:
#         username = re.search(SYSTEMUSERNAME, line)
#     if username:
#         username = username.group()
#         message = re.split(username, line)[-1]
#     else: message = re.split(TIMESTAMPEXPRESSION, line)[-1]

#     text.write(message)

# text.close()

text = open('chatmessages.txt', 'r').read()
quote = "Joe Biden is The President of the United States. He has many important duties." # open('chatmessages.txt', 'r').read()


textList = Text(nltk.word_tokenize(text))
for word in KEYWORDS:
    textList.concordance(word)