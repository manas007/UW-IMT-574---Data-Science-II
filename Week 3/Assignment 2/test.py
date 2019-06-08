import json

# Import the twitter library to interact with the Twitter APIs
import twitter

CONSUMER_KEY = 'xmfHc3KZTgAOBMJA0JO5ZwP8q'
CONSUMER_SECRET = '24X15Fqdm1inmNzxc0l8vIMcJ8ds6Re3iyzXAG1x3qu5RNOQU5'
ACCESS_TOKEN = '1089473531631493120-pk1JwMguQuik02EPX063YhTON4ZpW7'
ACCESS_SECRET = 'IyHSWFbnoM2dnK1ubXvl6lwMqmFW6FRBeiH7CTS0yb04K'

oauth = twitter.OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = twitter.TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
#iterator = twitter_stream.statuses.sample()

# You can also specify filters
# more detail: https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter.html
# and https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters
iterator = twitter_stream.statuses.filter(track= "Trump", language="en")

twitter = twitter.Twitter(auth=oauth)
            
# Search for latest tweets about "#marvel"
twitter.search.tweets(q='#marvel')