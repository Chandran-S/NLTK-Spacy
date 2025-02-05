
import requests
from bs4 import BeautifulSoup

# Example URL
url = 'https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-2/'



# Make a request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the article title
title = soup.find('h1').text

# Extract the article text
article_text = ''
for paragraph in soup.find_all('p'):
    article_text += paragraph.text + '\n'

# Print the title and article text
print(title)
print(article_text)

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# example text
text = ('''Impact of COVID-19 (Coronavirus) on the Indian Economy
The
corona outbreak has hit us hard. With the world economy suddenly coming to a
standstill, the future seems more uncertain. The pandemic has shown its worst
effect in the developed countries most. 
The following figure depicts the most affected countries as of March 31, 2020- (Source: WHO)
However,
the cases in India are still low, with total active cases under 1,500 as of 1st
April 2020, but the low number of tests performed remains a big issue of
concern.
The
following map shows the affected states in India – (Source: Ministry of health
and family welfare)
The
number may seem small, but if we closely have a look at the daily cases
reported, then the situation seems more alarming with the growth looking more
of exponential now.
 

The
number of cases no doubt are soon going to increase in the future, which is
hard to predict right now. But the curve is expected to be flatter in case of
India, as the lesson has been learnt from mistakes of countries like Italy and
a nation has been kept under a lockdown.
This was a necessary step, no doubt, but it has raised
more problems for an already slowdown hit country.
The Federation of Indian Chambers of Commerce and Industry (Ficci) said: “A significant 53 percent of Indian businesses indicate the marked impact of the coronavirus pandemic on business operations even at early stages.” The tourism and travel industry has been hit most whose operations have almost come down to zero. The second most hit sector is manufacturing, and with a significant portion of the unorganized sector being employed there, the situation worsens. Healthcare and hygiene products like mouth masks, sanitizers, and handwash have become expensive due to excessive demand.
With the present ongoing situation, the followings
things can be predicted:
The
Indian economy could react to corona crisis in 3 ways:
With the recent cut of India’s growth projections by Moody’s and Fitch, the future indicates a deeper slowdown, if not recession. To come out of this pandemic cleanly and with lesser shocks, the government needs to set its priorities right- with prime focus right now on the medical and healthcare sector as the country is battling against the coronavirus, but along with that, the government should try to take along the lower sections of the society providing them monetary gains as they are the one who is battling with the daily necessities along with the virus. In the long term, the government should keep an eye on the issue of liquidity to keep the cycle going. 
But above all this, we as a responsible citizen should
understand our duties and responsibilities towards the country and society and
try to take our country out of this outbreak by doing our part.
''')
scores = sid.polarity_scores(text)

# extract the positive and negative scores
positive_score = scores['pos']
negative_score = scores['neg']

print("Positive Score:", positive_score)
print("Negative Score:", negative_score)


# calculate the sentiment scores for each sentence
scores = sid.polarity_scores(text)

# extract the compound polarity score
polarity_score = scores['compound']

print("Polarity Score:", polarity_score)

from textblob import TextBlob

blob = TextBlob(text)
subjectivity_score = blob.sentiment.subjectivity

print("Subjectivity Score:", subjectivity_score)

import nltk
from nltk.tokenize import sent_tokenize

# example text

# tokenize the text into sentences
sentences = sent_tokenize(text)

# calculate the average sentence length
avg_sentence_length = sum(len(sentence.split()) for sentence in sentences) / len(sentences)

print("Average Sentence Length:", avg_sentence_length)

import nltk
from nltk.corpus import cmudict


# Load the dictionary
d = cmudict.dict()

def count_syllables(word):
    """
    Count the number of syllables in a word.
    """
    try:
        return max([len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]])
    except KeyError:
        # if word not found in the dictionary, assume it has one syllable
        return 1

def is_complex(word):
    """
    Determine whether a word is complex based on the number of syllables.
    """
    return count_syllables(word) >= 3

def percentage_complex_words(text):
    """
    Calculate the percentage of complex words in a text.
    """
    words = nltk.word_tokenize(text.lower())
    num_words = len(words)
    num_complex_words = len([word for word in words if is_complex(word)])
    return 100 * num_complex_words / num_words


print('percentage_complex_words',percentage_complex_words(text)) # Output: 60.0

from textstat import textstat
fog_index = textstat.gunning_fog(text)

print('FOG index:',fog_index)

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

sentences = sent_tokenize(text)
total_words = 0
for sentence in sentences:
    words = word_tokenize(sentence)
    total_words += len(words)

avg_words_per_sentence = total_words / len(sentences)
print('avg_words_per_sentence:',avg_words_per_sentence)

import re


def count_complex_words(text, complex_words):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text)

    # Count the number of complex words
    complex_word_count = sum(1 for word in words if word.lower() in complex_words)

    return complex_word_count
complex_words = ['analyze', 'sophisticated', 'articulate']

complex_word_count = count_complex_words(text, complex_words)
print('complex_word_count:',complex_word_count)

words = word_tokenize(text)
word_count = len(words)
print('word_count:',word_count)

import pyphen

# create a Pyphen object to hyphenate words
dic = pyphen.Pyphen(lang='en')


# split sentence into words
words = text.split()

# count syllables for each word
syllables_per_word = []
for word in words:
    syllables = dic.hyphenate(word)
    if syllables is not None:
        syllables_per_word.append(len(syllables.split("-")))


if syllables_per_word:
    avg_syllables_per_word = sum(syllables_per_word) / len(syllables_per_word)
else:
    avg_syllables_per_word = 0

print('avg_syllables_per_word:',avg_syllables_per_word)


import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


# Tokenize the text into words
words = word_tokenize(text)

# Tag each word with its part of speech
tagged_words = pos_tag(words)

# Find personal pronouns (tags starting with "PRP")
personal_pronouns = [word for word, tag in tagged_words if tag.startswith('PRP')]

# Count the number of personal pronouns
num_personal_pronouns = len(personal_pronouns)

# Print the results
print(f"Personal pronouns: {personal_pronouns}")
print(f"Number of personal pronouns: {num_personal_pronouns}")

