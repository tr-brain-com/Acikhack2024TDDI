import tweepy
import pandas as pd

# Twitter API anahtarlarınız
BEARER_TOKEN = 'xxxxxxxxxxxxx'

# Tweepy istemcisini oluşturun
client = tweepy.Client(bearer_token=BEARER_TOKEN)


def search_tweets(query, max_results, next_token=None):
    try:
        # Arama sorgusu
        response = client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=['lang', 'attachments'],
            expansions=['attachments.media_keys'],
            next_token=next_token
        )
        tweets = response.data
        media = response.includes.get('media', []) if response.includes else []
        next_token = response.meta.get('next_token') if response.meta else None

        tweet_data = []

        if tweets:
            for tweet in tweets:
                # Tweet'in dilini kontrol et ve medya içermediğinden emin ol
                has_media = False
                if hasattr(tweet, 'attachments') and tweet.attachments is not None:
                    media_keys = tweet.attachments.get('media_keys', [])
                    has_media = any(media_key in media_keys for media_key in media)

                if tweet.lang == 'tr' and not has_media:
                    tweet_data.append({'tweet_id': tweet.id, 'tweet_text': tweet.text})

        return tweet_data, next_token
    except tweepy.TweepyException as e:
        print(f"Error: {e}")
        return [], None


# Örnek kullanım
search_query = "#turkcell"
tweet_count = 100
all_tweets = []

# İlk sayfa için next_token olmadan başla
tweets, next_token = search_tweets(search_query, tweet_count)
all_tweets.extend(tweets)

# Daha fazla tweet çekmek için next_token kullan
while next_token:
    tweets, next_token = search_tweets(search_query, tweet_count, next_token)
    all_tweets.extend(tweets)
    if len(all_tweets) >= tweet_count:
        break

# Tweetleri CSV dosyasına kaydet
df = pd.DataFrame(all_tweets)
df.to_csv('tweet/turkcell _tweets_23062024.csv', index=False,sep='|')

print(f"{len(all_tweets)} tweets have been saved to tweets.csv")