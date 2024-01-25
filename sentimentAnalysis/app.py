from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyzeSentiment():
    data = request.json
    text = data.get("text", "")
    print("Received text: {}".format(text))
    sentiments = ["positive", "negative", "neutral"]
    return jsonify({"result": random.choice(sentiments)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)