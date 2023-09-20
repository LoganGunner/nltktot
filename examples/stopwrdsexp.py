from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

worf_quote = "Sir, I protest. I am not a merry man!"
# tokenize the string
words_in_quote = word_tokenize(worf_quote)
# sets the stops words to filter out
stop_words = set(stopwords.words("english"))
# list holds words that make it past the filter
filtered_list = []

# itterate to add words not in the stop words to the filtered list. 
# use .casefold() on word so you could ignore whether the letters in word were uppercase or lowercase.
# stopwords.words('english') includes only lowercase versions of stop words.
# certain words are in the stop words that may be neccesary for you analysis

for word in words_in_quote:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
print(filtered_list)

# you can also use a list comprehenstion to do the same
filtered_list = [ word for word in words_in_quote if word.casefold() not in stop_words]
print(filtered_list)