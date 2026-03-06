from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! \nThis is a simple Flask application running in a Docker container.'

@app.route('/login', methods=['POST'])
def login():
    return jsonify({
        "success": True,
        "user": {
            "name": "Max",
            "istAdmin": True,
            "istAbteilungsLeiter": True
        }
    })

if __name__ == '__main__':
    app.run(debug=True)