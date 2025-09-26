from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from calculator import berechne_fahrpreis, berechne_kinderpreis

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate_fare():
    data = request.json
    if 'distance' not in data:
        return jsonify({'error': 'Distance is required'}), 400
    
    try:
        distance = float(data['distance'])
        if distance <= 0:
            return jsonify({'error': 'Distance must be greater than 0'}), 400
            
        adult_fare = berechne_fahrpreis(distance)
        child_fare = berechne_kinderpreis(adult_fare)
        
        return jsonify({
            'distance': distance,
            'adult_fare': adult_fare,
            'child_fare': child_fare
        })
    except ValueError:
        return jsonify({'error': 'Invalid distance value'}), 400

if __name__ == '__main__':
    app.run(debug=True)