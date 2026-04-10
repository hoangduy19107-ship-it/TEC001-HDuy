import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'airports.json')

try:
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        airports_list = json.load(f)
except FileNotFoundError:
    airports_list = []

airports_by_icao = {
    airport['icao'].upper(): airport
    for airport in airports_list
    if 'icao' in airport
}

@app.route('/airport/<string:icao>')
def get_airport(icao):
    icao_code = icao.upper()
    airport = airports_by_icao.get(icao_code)
    if airport is None:
        return jsonify({'error': 'Airport not found'}), 404

    return jsonify({
        'icao': airport['icao'],
        'name': airport.get('name', ''),
        'city': airport.get('city', ''),
        'country': airport.get('country', '')
    })

if __name__ == '__main__':
    app.run(debug=True)
