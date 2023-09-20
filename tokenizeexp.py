from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

example_string = """Muad'Dib learned rapidly because his first training was in how to learn. And the first lesson of all was the basic trust that he could learn. It's shocking to find how many people do not believe they can learn, and how many more believe learning to be difficult."""
# tokenizes string by sentence
sentencetoke = sent_tokenize(example_string)
print(sentencetoke)
# tokenizes the string by word
wordtoke = word_tokenize(example_string)
print(wordtoke)
