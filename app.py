# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Helper function to filter and categorize input data
def process_data(data):
    numbers = []
    alphabets = []
    highest_lowercase = None
    
    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower() and (highest_lowercase is None or item > highest_lowercase):
                highest_lowercase = item
    
    highest_lowercase = [highest_lowercase] if highest_lowercase else []
    
    return numbers, alphabets, highest_lowercase

@app.route('/bfhl', methods=['POST'])
def post_bfhl():
    try:
        request_data = request.json
        data = request_data.get('data', [])
        
        numbers, alphabets, highest_lowercase = process_data(data)
        
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with dynamic values if needed
            "email": "john@xyz.com",  # Replace with dynamic values if needed
            "roll_number": "ABCD123",  # Replace with dynamic values if needed
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase
        }
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
