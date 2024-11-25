import threading
import time

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
                # десь будет логика торговли
                time.sleep(30)
            except Exception as e:
                print(f"Error in trading loop: {e}")
                time.sleep(5)
