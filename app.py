from flask import Flask, jsonify

app = Flask(__name__)

app.run(debug=False, host='0.0.0.0', port=8080)


@app.route('/hello', methods=["GET"])
def hello_world():
    return jsonify({'message': 'Hello, world'})

if __name__ == "__main__":
    app.run(debug=True)
