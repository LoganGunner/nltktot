from nltk import *
from constants import *


file = open('SeededChat.txt', 'r')

tracks = {}

for line in file.readlines():
    line = line.strip("\n")
    timestamp = re.search(TIMESTAMPEXPRESSION, line).group()
    username = re.search(USERNAMEEXPRESSION, line)
    if not username:
        username = re.search(SYSTEMUSERNAME, line)
    if username:
        username = username.group()
        message = re.split(username, line)[-1]
    else: message = re.split(TIMESTAMPEXPRESSION, line)[-1]

    tokens = [token.lower() for token in word_tokenize(message)]

    # Tag as relevant based on keyword
    if KEYWORDS[0].lower() in tokens:
        trackName = (' '.join(message.split(' ')[1:3]))
        newTrack = {'NAME': trackName }

        if trackName not in tracks.keys():
            tracks[trackName] = newTrack

        # Tag the start based on keyword
        if STARTINDICATOR in tokens:
            tracks[trackName]['START'] = timestamp[1:-2]
    
        # Tag the end based on keyword
        if ENDINDICATOR in tokens:
            tracks[trackName]['END'] = timestamp[1:-2]

print(tracks)