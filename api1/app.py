from flask import Flask, jsonify
import requests

app = Flask(__name__)

API2_URL = 'http://api2:5002/hello'

@app.route('/proxy')
def proxy():
    print("API1: Received request from User")
    try:
        response = requests.get(API2_URL)
        print("API1: Forwarded request to API2")
        print(f"API1: Response from API2: {response.text}")
        return jsonify({"from_api2": response.json()}), 200
    except Exception as e:
        print(f"API1: Error contacting API2: {e}")
        return jsonify({"error": "API2 not reachable"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
