
import requests
from bs4 import BeautifulSoup

# Example URL
url = 'https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-3/'
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
From the economic point of
view, India is confronted today with perhaps its greatest emergency since independence. The global financial
crisis in 2008-09 was a gigantic demand shock, but our workers could still get-up-and-go to work, our firms were coming off years of steady growth, our financial system was largely sound, and our government finances were blooming. None of this is true today as
we fight the
coronavirus pandemic. Yet
there is also no reason to
despair. With the right undertakings and
priorities, and drawing on India’s many sources of strength, it can kill this virus back, and even set the stage for a much more hopeful tomorrow.
The rampant spread of COVID-19 outbreak, across borders and geographies, has severely impacted almost the whole world and triggered significant downside risks to the overall global economic outlook. Steps taken to contain its spread, such as the nationwide lockdown announced by the Indian Government, have brought economic activity to a near – standstill with impacts on both consumption and investment. India’s real GDP growth decelerated to its lowest in over 6 years in 3Q 2019 – 2020 and the outbreak of COVID – 19 posted fresh challenges. For most businesses, the slowdown could be in the form of supply disruptions, fall in consumption demand, and stress on the banking and financial sectors. In sum the three major contributors to GDP will all get affected i.e. Private Consumption, Investment and External Trade.
Figure 1.1: Showing quarterly growth in GDP (in %). Source: MoSPI
Assessing the exact impact for India is hard
with uncertainty on how long the pandemic would last. Three likely scenarios for India’s economic situation could be:
            Figure 1.2: Showing an optimistic situation. Source: Deloitte
Figure 1.3: Showing an optimistic scenario with a severe and extended impact of COVID-19. Source: Deloitte
In scenario 2, inflation picks up in H2 FY
2021 as demand revives faster than supply. Inflation may increase above the
target range (4 percent) for a short time in FY 2021 because of economic
overheating. In this scenario, inflation remains 3-4 percent during this period
despite weak demand because of a sharper fall in production.
Figure 1.4: Showing pessimistic situation, with a
prolonged severe downturn. 
Source: Deloitte.
Impact on the Demand side:
Impact on the Supply side:
           
Figure 1.5: Showing supply
chain disruptions. Source: The Economic
Times.
What has been done so far?
India has already undertaken the following
measures to counter the impact from of the pandemic:
What can the Corporates do?
The crisis is a story with an uncertain ending. However, what is clear that the COVID-19 has introduced new challenges to the business environment which called for a measured, practical and informed approach from political and business leaders. A company needs to think and act across five horizons:
Figure
1.6: Showing the
crisis as a lesson to businessmen in assessing risk to their business. Source: The Economic Times 
Collectively, these five stages epitomize the inescapable of our time: the battle
against COVID-19 is one that leaders today must win in order to find an economically
and socially feasible path to the next normal.
What can the government do?
The government should consider certain measures in order to manage the pandemic. The following steps and the recognition of the likely scenarios for the Indian economy can enable policymakers to identify appropriate countermeasures to stem the spread of the pandemic:
Therefore, the question remains whether the stimulus is enough or not – both quantitatively and qualitatively? Would it be able to help the economy absorb the shock of the lockdown? Compared to what the USA (2 trillion USD), Germany (610 billion USD), UK (424 billion USD), France (335 billion USD), Spain (218 billion USD), China (78.8 billion USD) and Italy (27.3 billion USD), the spending by India (1, 70,000 crore – 22.5 billion USD) may prima facie appear to be insufficient. However, such a comparison is not easy and straightforward because a lot of factors are to be taken into account. In addition, the important factor that needs to be considered is whether at this point in time the country is able to spend more than this or not. Against a revised budget estimate of Rs. 21,63,000 crore for 2019-20 towards Tax collections, the collection as on 31st Dec 2019 was to the tune of Rs. 13,83,000 crore only with a clearly huge shortfall. In addition, a substantial amount would also have to be spent now to tackle the pandemic which is of utmost priority. On top of it, huge additional spending would jeopardize the fiscal deficit discipline although, at times of emergency, fiscal deficit should not be a matter of concern at all.
 It would also have to be seen how long this virus continues to affect India and going by the hygiene standard and herd mentality that we have, the virus continues to affect us beyond 3 months and extends to 6-8 months, quite obviously these packages would be grossly insufficient and more money will have to be pumped into the economy. If the need arises, currency notes will have to be printed and circulated and concerns about higher fiscal deficit should be simply pushed to the backseat. The corporate sector and a section of large-hearted people have also come forward at this time of distress to support the government initiatives in fighting this menace which should provide some financial comfort to the Government.
The pandemic has appeared from nowhere as a potential death knell to the World economy which is already under stress and India is no exception. There is no second opinion that this pandemic has hit the world very hard and would continue to do so in the foreseeable future. Whether India can emerge from the medical pandemic as well as the economic pandemic relatively unscathed remains to be seen. We will have to take care of our lives as well as the livelihoods of our citizens. As Indians, we hope, we shall overcome.  Together we can do this and we will.
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

