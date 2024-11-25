from flask import Flask, render_template, jsonify, request, redirect, url_for
import os
from datetime import datetime
from src.bot.trading_bot import BitcoinTradingBot
from collections import deque

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')

# Initialize bot
bot = BitcoinTradingBot(
    api_key=os.environ.get('KRAKEN_API_KEY'),
    api_sec=os.environ.get('KRAKEN_API_SECRET'),
    test_mode=True
)

# Price history storage
price_history = {
    'times': [],
    'prices': []
}

@app.route('/')
def index():
    current_price = bot.get_current_price()
    if current_price:
        price_history['times'].append(datetime.now().strftime('%H:%M:%S'))
        price_history['prices'].append(current_price)
        
        # Keep only last 20 points
        if len(price_history['times']) > 20:
            price_history['times'] = price_history['times'][-20:]
            price_history['prices'] = price_history['prices'][-20:]

    portfolio = {
        'balance': bot.balance,
        'btc_amount': bot.btc_amount,
        'current_price': current_price,
        'last_update': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    settings = {
        'buy_threshold': bot.buy_threshold,
        'sell_threshold': bot.sell_threshold
    }

    return render_template('dashboard.html',
                         balance=portfolio['balance'],
                         btc_amount=portfolio['btc_amount'],
                         current_price=portfolio['current_price'],
                         last_update=portfolio['last_update'],
                         trades=bot.trades,
                         settings=settings,
                         is_running=bot.is_running)

@app.route('/settings', methods=['POST'])
def update_settings():
    if not bot.is_running:
        bot.buy_threshold = float(request.form.get('buy_threshold', -0.5))
        bot.sell_threshold = float(request.form.get('sell_threshold', 0.5))
    return redirect(url_for('index'))

@app.route('/toggle', methods=['POST'])
def toggle_bot():
    if bot.is_running:
        bot.stop()
    else:
        bot.start()
    return redirect(url_for('index'))

@app.route('/api/price_history')
def get_price_history():
    return jsonify({
        'labels': price_history['times'],
        'prices': price_history['prices']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
