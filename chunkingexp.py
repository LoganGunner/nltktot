from nltk.tokenize import word_tokenize
import nltk


lotr_quote = "It's a dangerous business, Frodo, going out your door."
# before chunking you need to make sure that the parts of speech are tagged
words_in_lotr_quote = word_tokenize(lotr_quote)

lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)

#  you must define the grammar chunk first. it is a combination of rules typically using regex

grammar = "NP: {<DT>?<JJ>*<NN>}"

# create the chunk parser
chunk_parser = nltk.RegexpParser(grammar)

tree = chunk_parser.parse(lotr_pos_tags)

tree.draw()