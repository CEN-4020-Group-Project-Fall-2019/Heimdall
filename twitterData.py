# import api
import twitter

# login to api with security keys 
api = twitter.Api(consumer_key= 'Z4HlCdEhEJk8SlLHzsZDx9fxw', consumer_secret='xLM61gbcSy3InKE7QCVfhZHDstYaPBJNdMBTBC9cfl11BgM27X' , access_token_key='977249287-f4r7WLtpa15LaxsXNOsNk7fT8pGc0NHchC5vzPl1', access_token_secret='aAMDaG7OcdqbebajEYSXDcTAbTimlLnV9InRdUpkFqP0U')

#open file for result output
f = open('test.txt', 'w')

#search twitter for keyword (term)
searchResults = api.GetSearch(term='elon musk', include_entities=True)

#write results to file from list one at a time
([f.write(s.text) for s in searchResults])

#close results file and exit script
f.close()
exit()
