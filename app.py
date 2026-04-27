from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
from db import get_potlas_games

app = Flask(__name__)
CORS(app)

@app.route('/')
def main_page():
    return '<h2>supabase db <-> power bi report project</p>'


@app.route('/trigger')
def trigger_script():
    p = subprocess.run(
        ["C:\\Program Files\\Python313\\python.exe", "C:\\Projekt\\db-powerbi\\db.py"],
        capture_output=True,
        text=True)

    return jsonify({"response": f"{p.returncode} {p.stderr}"})

@app.route('/potlas')
def potlas():
    data = get_potlas_games()

    with open('C:/Projekt\\potlas-weboldal\\src\\backend\\DropdownOptions.ts', 'w') as file:
        file.write(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=False, use_reloader=False)