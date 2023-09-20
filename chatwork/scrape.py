import nltk
import re
from nltk.corpus import stopwords

###################################[ Constants ]######################################

USERNAMEEXPRESSION = "<[A-Za-z0-9]+>"
SYSTEMUSERNAME = "-!-"
TIMESTAMPEXPRESSION = "\[[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?\]"
KEYWORDS = [ # List of Keywords to reference
    'keyboard', 'key'
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

text = "Joe Biden is The President of the United States. He has many important duties." # open('chatmessages.txt', 'r').read()

stop_words = set(stopwords.words("english"))

class namedEntity :
    def __init__(self, word:str) -> None:
        '''Takes in a word and created a new object with blank alias and timeline fields to track mentions'''
        self.__repr__ = word
        self.name = word
        self.alias = set()
        self.timeline = []

    def add_alias(self, word:str):
        self.alias.add(word)

    def add_event(self, message:str):
        self.timeline.append(message)


def extract_ne(quote:str):
    '''Iterates through a text or quote and returns a set of named entities as a list of strings'''
    words = nltk.word_tokenize(quote)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    return set(
        " ".join(i[0] for i in t)
        for t in tree
        if (hasattr(t, "label") and t.label() == "NE") or (hasattr(t, "label") and t.label == "NNP")
    )

print(extract_ne(text))





