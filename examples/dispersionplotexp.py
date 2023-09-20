import nltk
from nltk.book import text8
# draws a dipsersion plot with a blue line for each instance of the word and shows were in the text the word is used
text8.dispersion_plot(["woman","lady","girl","gal","man","gentleman","boy","guy"])