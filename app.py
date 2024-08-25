# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

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
def process_data():
    data = request.json.get('data', [])
    
    # Example processing - You would implement your actual processing logic here
    alphabets = [item for item in data if item.isalpha()]
    numbers = [item for item in data if item.isdigit()]
    lowercase_letters = sorted([item for item in data if item.islower()])
    highest_lowercase = lowercase_letters[-1] if lowercase_letters else None
    
    return jsonify({
        'alphabets': alphabets,
        'numbers': numbers,
        'highest_lowercase': highest_lowercase
    })

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
