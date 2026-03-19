from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return '<h2>supabase db <-> power bi report project</h2><br><p>get orders: <a href="/orders">Click here</a>'

@app.route('/orders')
def get_orders():
    return send_file(path_or_file='orders.json',
                     as_attachment=True,
                     download_name='orders.json',
                     mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)