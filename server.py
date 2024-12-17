from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/<name>', methods=['GET'])
def hello(name):
    return jsonify({"message": f"Hi {name}"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
