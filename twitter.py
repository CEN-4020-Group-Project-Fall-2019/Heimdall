# pip installed all the things the documentation for this library told me to
import twitter

# twitter for python API online says this is the correct way to access this
api = twitter.Api(consumer_key='gew3hxmZ6gBXQb8xWhGsf3pjC', consumer_secret='gf4hTgIEwdZm40kIH78txmD2tIsNKLxEtX1Iz8rypN0yEYMEjM', access_token_key='977249287-RyoGmxMmZpyRQboByP8HoMt3NIJHgWU9ON0wWd43 ', access_token_secret='E3w2puREG5Nywhky5ckF2pavXmskIAEO19QJSmtTkhaDP')

# when above errors are figured out this should print a list of strings;
#  each string is a tweet containing the word or words that are input.
#  once tested this will output to a string to be used in the
# natural language processor
print(api.GetSearch(term = "Elon Musk"))