import tweepy, requests, json, time
coins = []
coins.append("bitcoin")
coins.append("ethereum")
coins.append("dogecoin")
coins.append("monero")

consumer_key = "BLANK"
consumer_secret = "BLANK"
access_key = "BLANK"
access_secret = "BLANK"

def publish_tweet(tweet):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    my_post = str(tweet)
    api.update_status(status=my_post)

def get_data( cryptocurrency ):
    data = requests.get('https://api.coinmarketcap.com/v1/ticker/%s/'%(cryptocurrency))
    data = json.loads(data.text)
    
    tweet = (
        "Cryptocurrency: #" + data[0]['name'] + "\n" +
        "Price USD: " + data[0]['price_usd'] + "\n" +
        "Price BTC: " + data[0]['price_btc'] + "\n" +
        "24h Volume USD: " + data[0]['24h_volume_usd'] + "\n" +
        "Percent change 24h: " + data[0]['percent_change_24h'] )
    print(tweet + "\n")
    publish_tweet(tweet)
    
def main():
    print("Welcome to PythonCrytoBot for twitter \n")
    while(True):
        for x in range(0,len(coins)):
            get_data(coins[x])            
            time.sleep(25)
        time.sleep(3600)

    
    
if __name__ == "__main__":
    main()


