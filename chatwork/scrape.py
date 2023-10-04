from nltk import *
from constants import *

def track_scrape(filename:str, 
                 TIMESTAMPEXPRESSION=TIMESTAMPEXPRESSION, 
                 USERNAMEEXPRESSION=USERNAMEEXPRESSION, 
                 SYSTEMUSERNAME=SYSTEMUSERNAME,
                 KEYWORDS:list=KEYWORDS,
                 INDICATORS:list=INDICATORS): 
    '''Open a .txt file of plaintext IRC logs, returns a nested dictionary containing the GANTT information of tracks in the chat.'''

    file = open(filename, 'r')

    tracks = {}

    for line in file.readlines():

        line = line.strip("\n")

        if line:

            timestamp = re.search(TIMESTAMPEXPRESSION, line).group()[1:-2]
            username = re.search(USERNAMEEXPRESSION, line)
            
            if not username:

                username = re.search(SYSTEMUSERNAME, line)
            if username:

                username = username.group()
                message = re.split(username, line)[-1].strip()
                
            else: message = re.split(TIMESTAMPEXPRESSION, line)[-1].strip()

            tokens = [token.lower() for token in word_tokenize(message)]

            # Tag as relevant based on keyword
            for keyword in KEYWORDS:

                if keyword.lower() in tokens:

                    trackName = (' '.join(message.split(' ')[0:2]))
                    newTrack = {'NAME': trackName }

                    if trackName not in tracks.keys():

                        tracks[trackName] = newTrack

                    # Tag the actions based on keywords

                    for list in INDICATORS:

                        for indicator in list:
                            if list == STARTINDICATORS: # Check for starts

                                typeKey = 'START'

                            elif list == ENDINDICATORS: # Check for Ends

                                typeKey = 'END'

                            elif list == SUBTASKINDICATORS: # Check for miscellaneous actions

                                typeKey = indicator.upper()
                                
                            if indicator in tokens:

                                if typeKey not in tracks[trackName].keys():

                                    tracks[trackName][typeKey] = [timestamp]

                                else:

                                    tracks[trackName][typeKey] = tracks[trackName][typeKey]
                                    tracks[trackName][typeKey].append(timestamp)
                
    return tracks

print(track_scrape('SeededChat.txt'))