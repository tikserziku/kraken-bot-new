import threading
import time
import requests

class BitcoinTradingBot:
    def __init__(self, api_key=None, api_sec=None, test_mode=True):
        self.test_mode = test_mode
        self.api_key = api_key
        self.api_sec = api_sec
        self.trades = []
        self.balance = 10000
        self.btc_amount = 0
        self.is_running = False
        self.trading_thread = None
        self.buy_threshold = -0.5  # Меняем на 0.5%
        self.sell_threshold = 0.5  # Меняем на 0.5%

    def get_current_price(self):
        try:
            response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
            if response.status_code == 200:
                return response.json()["bitcoin"]["usd"]
        except Exception as e:
            print(f"Error getting price: {e}")
        return None

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.trading_thread = threading.Thread(target=self._trading_loop)
            self.trading_thread.daemon = True
            self.trading_thread.start()

    def stop(self):
        self.is_running = False
        if self.trading_thread:
            self.trading_thread.join(timeout=5)
            self.trading_thread = None

    def _trading_loop(self):
        while self.is_running:
            try:
                current_price = self.get_current_price()
                if current_price:
                    print(f"Current BTC price: ${current_price}")
                time.sleep(30)
            except Exception as e:
                print(f"Error in trading loop: {e}")
                time.sleep(5)
