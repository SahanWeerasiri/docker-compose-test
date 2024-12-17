from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/<name>', methods=['GET'])
def hello(name):
    return jsonify({"message": f"Hi {name}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
