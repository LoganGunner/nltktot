from nltk.tokenize import word_tokenize
import nltk

# chinking is a sort of sub off shoot of chunking
lotr_quote = "It's a dangerous business, Frodo, going out your door."

words_in_lotr_quote = word_tokenize(lotr_quote)
lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)

#  you must define the grammar first. it is a combination of rules typically using regex

grammar = """
Chunk: {<.*>+} 
        }<JJ>{"""

# create the chunk parser
chunk_parser = nltk.RegexpParser(grammar)

tree = chunk_parser.parse(lotr_pos_tags)

tree.draw()