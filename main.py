from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Тарифная сетка буста гильдий
BOOST_PACKAGES = {
    1: {
        "title": "1 Отряд",
        "bots": 4,
        "diamonds": 310,
        "tag": "Старт",
        "popular": False,
        "color": "#00f2fe"
    },
    2: {
        "title": "2 Отряда",
        "bots": 8,
        "diamonds": 520,
        "tag": "Популярный",
        "popular": True,
        "color": "#ff007f"
    },
    3: {
        "title": "3 Отряда",
        "bots": 12,
        "diamonds": 720,
        "tag": "Выгодный",
        "popular": False,
        "color": "#00ff88"
    },
    4: {
        "title": "4 Отряда",
        "bots": 16,
        "diamonds": 1060,
        "tag": "Ультра-Буст 🔥",
        "popular": False,
        "color": "#ffaa00"
    }
}


@app.route('/')
def index():
    return render_template('index.html', packages=BOOST_PACKAGES, telegram_handle="klayener")


@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json or {}
    squads = int(data.get('squads', 1))

    if squads in BOOST_PACKAGES:
        pkg = BOOST_PACKAGES[squads]
        return jsonify({
            'success': True,
            'squads': squads,
            'bots': pkg['bots'],
            'diamonds': pkg['diamonds'],
            'telegram_url': f"https://t.me/klayener?text=Привет!%20Хочу%20заказать%20{pkg['title']}%20({pkg['bots']}%20ботов)%20за%20{pkg['diamonds']}%20алмазов."
        })
    return jsonify({'success': False, 'message': 'Выбор от 1 до 4 отрядов'}), 400


if __name__ == '__main__':
    print("🚀 3D-Сайт Free Fire Boost запущен на http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)