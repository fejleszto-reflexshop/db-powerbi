from flask import Flask, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

ORDERS_FILE = 'R:/orders.json'

@app.route('/')
def hello_world():
    return '<h2>supabase db <-> power bi report project</h2><br><p>get orders: <a href="/orders">Click here</a></p>'

@app.route('/orders')
def get_orders():
    return send_file(
        path_or_file=ORDERS_FILE,
        as_attachment=True,
        download_name='orders.json',
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=False, use_reloader=False)