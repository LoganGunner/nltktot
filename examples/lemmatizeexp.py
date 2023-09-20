from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

# lemmatize returns the whole base word instead of stemming which can return partials of a word
lemmatizer.lemmatize('scarves')


string_for_lemmatizing = "The friends of DeSoto love scarves"
# tokenize the words to separate them individualy
words = word_tokenize(string_for_lemmatizing)
# use a list comprehension to lemmatize the words
lemmatized_words =[lemmatizer.lemmatize(word) for word in words]

print(lemmatized_words)

# There is a pos = "" for making sure a word is treated as it should such as adj. at base it reads them as nouns.