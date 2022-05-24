import helper_functions
import random

# Open list of quotes from arrested development
with open('arrested_development.txt') as file:
    ad = file.read()
ad = ad.split(',')

# Randomly select a quote and run it through the bigram poem function
phrase = random.choice(ad)
ad_poem = helper_functions.bigram_poem(phrase)

print(ad_poem)
