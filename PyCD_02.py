import tweepy
from textblob import TextBlob
import csv

consumer_key = "Consumer Key"
consumer_secret = "Consumer Secret Key"
access_token = "Access Token Key"
access_token_secret = "Access Token Secret Key"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet_topic = input("Qual tópico deseja procurar?: ")

public_tweets = api.search(tweet_topic)

#Abrindo o arquivo dataset.csv com os tweets
with open('dataset.csv', mode='w') as tweets_file:
    tweet_writer = csv.writer(tweets_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

    tweet_writer.writerow(['Tweet', 'Author', 'Date', 'Sentiment Polarity'])
    
    for tweet in public_tweets:
        tweet_text = tweet.text
        tweet_user = tweet.user.name
        tweet_date = tweet.date
        tweet_sentiment = TextBlob(tweet_text).sentiment.polarity
        print(tweet_text, tweet_user, tweet_date)
        print("Sentiment is %f" % tweet_sentiment)
        tweet_writer.writerow([tweet_text, tweet_user, tweet_date, tweet_sentiment])
        
