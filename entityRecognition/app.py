from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recognize', methods=['POST'])
def recognizeEntities():
    data = request.json
    text = data.get("text", "")
    print("Received text: {}".format(text))
    return jsonify({"result": "simulated entity recognition result"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8003)