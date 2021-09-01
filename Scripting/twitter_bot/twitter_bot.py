import tweepy
import time

auth = tweepy.OAuthHandler('', '') # API key and API secret key from Twitter API
auth.set_access_token('', '') # Access token and Acess token secret from Twitter API

api = tweepy.API(auth)

# generator: in case rate limit is reached, there will a pause of 500ms
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(500)

# follow back function
def follow_back(follower_username):
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        if follower.name == follower_username:
            follower.follow()
            print(f'Following {follower_username}.')
            break
        else:
            print('f{follower_username} is not your follower.')
    
# like tweet function
def like_tweet(search_string, number_of_tweets):
    for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(number_of_tweets)):
        try:
            tweet.favorite()
            print('I like that tweet!')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# retweet tweet function
def retweet_tweet(search_string, number_of_tweets):
    for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(number_of_tweets)):
        try:
            tweet.retweet()
            print('Retweeted!')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

if __name__ == '__main__':
    # follow_back('') # function with one argument: twitter username
    # like_tweet('', ) # function with two arguments: string to search and number of tweets to like
    # retweet_tweet('', ) # function with two arguments: string to search and number of tweets to retweet
    pass # comment this line when a function from above is used
