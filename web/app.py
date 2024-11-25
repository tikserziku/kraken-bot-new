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
    current_price = bot.get_current_price() or 40000
    portfolio = {
        'balance': bot.balance,
        'btc_amount': bot.btc_amount,
        'current_price': current_price,
        'last_update': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Trading settings
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
        new_buy = float(request.form.get('buy_threshold', -0.5))
        new_sell = float(request.form.get('sell_threshold', 0.5))
        app.logger.info(f"Old settings: buy={bot.buy_threshold}, sell={bot.sell_threshold}")
        app.logger.info(f"New settings: buy={new_buy}, sell={new_sell}")
        bot.buy_threshold = new_buy
        bot.sell_threshold = new_sell
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


