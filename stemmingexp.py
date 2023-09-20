from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

string_for_stemming = """The crew of the USS Discovery discovered many discoveries. Discovering is what explorers do."""

# before being able to stem the words you must separate the words
words = word_tokenize(string_for_stemming)

# Create a list of the stemmed versions of the words in words by using stemmer.stem() in a list comprehension
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)

# beware of over stemming and understemming