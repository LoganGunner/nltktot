from nltk.tokenize import word_tokenize
import nltk

sagan_quote = """If you wish to make an apple pie from scratch, you must first invent the universe."""

words_in_sagan_quote = word_tokenize(sagan_quote)

tagged_words = nltk.pos_tag(words_in_sagan_quote)
print(tagged_words)

# nltk.help.upenn_tagset() shows a list of tags and their meanings

