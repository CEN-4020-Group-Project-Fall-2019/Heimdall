import feedparser
import argparse
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import argparse

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('stock_name', help='The subject you\'d like to analyze.')
args = parser.parse_args()

python_wiki_rss_url = "https://news.google.com/rss/search?q={" + args.stock_name + "}"

feed = feedparser.parse( python_wiki_rss_url )

score = 0
for i in range(0, 20):
        client = language.LanguageServiceClient()
        content = feed.entries[i]["summary"]
        document = types.Document(content=content, type=enums.Document.Type.HTML)
        annotations = client.analyze_sentiment(document=document)
        score += annotations.document_sentiment.score

print(score/20)
