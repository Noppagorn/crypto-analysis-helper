from urllib.request import urlopen
import json
def getDataFromMessari(coin):
    import urllib
    url = "https://data.messari.io/api/v1/assets" + "/" + coin.get('symbol') + "/" + coin.get("type")
    request_text = urllib.request.urlopen(url).read().decode("utf-8")
    phrase = json.loads(request_text)
    print(json.dumps(phrase, indent=4, sort_keys=True))

if __name__ == '__main__':
    btc = {
       'symbol': "BTC",
        'type': "metrics",
    }

    eth = {
        'symbol': "ETH",
        'type': "metrics",
    }
    getDataFromMessari(btc)
