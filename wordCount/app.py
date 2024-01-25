from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/count', methods=['POST'])
def wordCount():
    data = request.json
    text = data.get("text", "")
    print("Received text: {}".format(text))
    return jsonify({"result": len(text.split())})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8002)