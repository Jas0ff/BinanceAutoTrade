import ccxt
import config
binance = ccxt.binance({
    'apiKey':config.API_KEY,
    'secret':config.API_SECRET,
    'password':config.PASSPHARSE
})
#options 變交易永續合約(BTC/USDT x5)
binance.options = {
    'defaultType':'future',
    'adjustForTimeDifference': True,
    'defaultTimeInForce': 'GTC'
}
#---------------------------------------
def trade_crypto(request):
    succeedtag= "order succeed"
    data = request.get_json()
    if 'password' not in data or data['password'] != config.TRADINGVIEW_PASSPHRASE:
        print("error,invalid log in.")
        return "error, invalid log in."
    try:
        tickers={
            "BTCUSDT":"BTC/USDT",
            "ETHUSDT":"ETH/USDT",
            "APEUSDT":"APE/USDT",
            "AVAXUSDT":"AVAX/USDT",
            "BTCUSDTPERP":"BTC/USDT"
        }
        ticker=tickers[data['ticker']]

        binance.create_market_order(ticker,data['strategy']['order_action'].upper(),data['strategy']['order_contracts'])
        print(data['script']+"\norder successful.")
    except Exception as e:
        print(data['script']+"\norder error.")
        succeedtag="order fail"
        print(e)

    return succeedtag