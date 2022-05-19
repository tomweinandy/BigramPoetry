import random
import bigram

with open('arrested_development.txt') as file:
    ad = file.read()

ad = ad.split(',')
phrase = random.choice(ad)

print(bigram.bigram_poem(phrase))

