from flask import Flask, render_template, jsonify, request, redirect, url_for
import os
from datetime import datetime
from src.bot.trading_bot import BitcoinTradingBot

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')

# Initialize bot
bot = BitcoinTradingBot(
    api_key=os.environ.get('KRAKEN_API_KEY'),
    api_sec=os.environ.get('KRAKEN_API_SECRET'),
    test_mode=True
)

@app.route('/')
def index():
    # Get current bot status
    portfolio = {
        'balance': 10000,
        'btc_amount': 0.5,
        'current_price': 40000,
        'last_update': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Sample trades data
    trades = [
        {
            'timestamp': '2024-11-25 10:00:00',
            'type': 'buy',
            'price': 39000,
            'amount': 0.1
        },
        {
            'timestamp': '2024-11-25 09:00:00',
            'type': 'sell',
            'price': 41000,
            'amount': 0.05
        }
    ]

    # Trading settings
    settings = {
        'buy_threshold': -2.0,
        'sell_threshold': 2.0
    }

    return render_template('dashboard.html',
                         balance=portfolio['balance'],
                         btc_amount=portfolio['btc_amount'],
                         current_price=portfolio['current_price'],
                         last_update=portfolio['last_update'],
                         trades=trades,
                         settings=settings,
                         is_running=bot.is_running)

@app.route('/settings', methods=['POST'])
def update_settings():
    if not bot.is_running:
        bot.buy_threshold = float(request.form.get('buy_threshold', -2.0))
        bot.sell_threshold = float(request.form.get('sell_threshold', 2.0))
    return redirect(url_for('index'))

@app.route('/toggle', methods=['POST'])
def toggle_bot():
    if bot.is_running:
        bot.stop()
    else:
        bot.start()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


