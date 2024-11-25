class BitcoinTradingBot:
    def __init__(self, api_key=None, api_sec=None, test_mode=True):
        self.test_mode = test_mode
        self.api_key = api_key
        self.api_sec = api_sec
        self.trades = []
        self.balance = 10000
        self.btc_amount = 0
