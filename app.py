from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
from db import get_potlas_games
import time

app = Flask(__name__)
CORS(app)

def run_script(path: str) -> str:
    p = subprocess.run(
        ["C:\\Program Files\\Python313\\python.exe", path],
        capture_output=True,
        text=True)
    
    return f"{p.returncode} {p.stderr}"


@app.route('/')
def main_page():
    return '<h2>supabase db <-> power bi report project</p>'


@app.route('/trigger')
def trigger_script():
    r = run_script("C:\\Projekt\\db-powerbi\\db.py")

    return jsonify({"response": r})

@app.route('/potlas')
def potlas():
    data = get_potlas_games()

    with open('C:\\Projekt\\potlas-weboldal\\src\\backend\\DropdownOptions.ts', 'w', encoding='utf-8') as file:
        file.write(data[0]['html_code'])

    time.sleep(1)

    r = run_script("C:\\Projekt\\potlas-weboldal\\upload.py")
    
    return jsonify({'response': r})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=False, use_reloader=False)