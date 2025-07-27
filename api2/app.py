from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    print("API2: Received request from API1")
    return jsonify({"message": "Hello from API2"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
