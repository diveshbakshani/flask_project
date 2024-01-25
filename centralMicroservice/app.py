from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

# having some simulation of persistency as a list
microservices = {
    "sentiment-analysis": "http://sentiment_analysis:8001/analyze",
    "word-count": "http://word_count:8002/count",
    "entity-recognition": "http://entity_recognition:8003/recognize"
}

@app.route('/services', methods=['GET'])
def list_services():
    return jsonify(list(microservices)) # returning services in GET /services endpoint

@app.route('/services', methods=['POST'])
def register_service():
    data = request.json
    
    if 'name' not in data or 'url' not in data:
        return jsonify({"error": "Please provide both name and url"}), 400

    microservices[data['name']] = data['url']
    return jsonify({"message": "Service registered successfully"}), 200


@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.json
    serviceName = data['service']
    text = data['text']

    if serviceName not in microservices:
        return jsonify({"error": "Requested service does not exist"}), 404

    print(microservices[serviceName])
    response = requests.post(microservices[serviceName], json={"text": text}) # passing along message to the respective microservice
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)