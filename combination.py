# import api
import twitter

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# login to api with security keys
api = twitter.Api(consumer_key= 'Z4HlCdEhEJk8SlLHzsZDx9fxw', consumer_secret='xLM61gbcSy3InKE7QCVfhZHDstYaPBJNdMBTBC9cfl11BgM27X' , access_token_key='977249287-f4r7WLtpa15LaxsXNOsNk7fT8pGc0NHchC5vzPl1', access_token_secret='aAMDaG7OcdqbebajEYSXDcTAbTimlLnV9InRdUpkFqP0U')

#open file for result output
f = open('test.txt', 'w')

#search twitter for keyword (term)
searchResults = api.GetSearch(term='elon musk', include_entities=True)

#write results to file from list one at a time
([f.write(s.full_text) for s in searchResults])


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    # checks sentiment of each tweet

    # for index, sentence in enumerate(annotations.sentences):
    #     sentence_sentiment = sentence.sentiment.score
    #     print('Sentence {} has a sentiment score of {}'.format(index, sentence_sentiment))

    # can be changed later to just return overall score
    print('Overall Sentiment: score of {} with magnitude of {}'.format(score, magnitude))
    return 0


def analyze(filename):
    client = language.LanguageServiceClient()

    with open(filename, 'r') as review_file:
        content = review_file.read()

    document = types.Document(content=content, type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    print_result(annotations)


if __name__ == '__main__':
    analyze('test.txt')


#close results file and exit script
f.close()
exit()
