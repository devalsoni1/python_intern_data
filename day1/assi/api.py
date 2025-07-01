from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Example data
    data = {
        "message": "Hello, world!",
        "status": "success"
    }
    return jsonify(data), 200

@app.route('/data', methods=['POST'])
def post_data():
    # Get JSON data from the request
    input_data = request.get_json()

    # Process the data (here we just return it)
    response_data = {
        "received": input_data,
        "message": "Data received successfully!",
        "status": "success"
    }

    return jsonify(response_data), 201

if __name__ == '__main__':
    app.run(debug=True)