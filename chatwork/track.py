from nltk import *


def textify(filename):
    # read text
    text = open(filename, "r").read()
    tokens = word_tokenize(text)
    textList = Text(tokens)
    return textList

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
    words = word_tokenize(quote)
    tags = pos_tag(words)
    tree = ne_chunk(tags, binary=True)
    return set(
        " ".join(i[0] for i in t)
        for t in tree
        if (hasattr(t, "label") and t.label == "NE") or (hasattr(t, "label") and t.label == "NNP")
    )

