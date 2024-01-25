import json
import requests
import pytest

BASE_URL = "http://localhost:8000"

def test_get_services():
    url = f"{BASE_URL}/services"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "sentiment-analysis" in response.json()

def test_post_service():
    url = f"{BASE_URL}/services"
    data = {"name": "new-service", "url": "http://localhost:8000/new-service"}
    response = requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert "message" in response.json()

def test_post_service_fail():
    url = f"{BASE_URL}/services"
    data = {"url": "http://localhost:8000/new-service"}
    response = requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert "error" in response.json()

def test_analyze_sentiment():
    url = f"{BASE_URL}/analyze"
    data = {"service": "sentiment-analysis", "text": "This is a test text."}
    response = requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert "result" in response.json()

def test_analyze_wc():
    url = f"{BASE_URL}/analyze"
    data = {"service": "word-count", "text": "This is a test text."}
    response = requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert "result" in response.json()

def test_sentimentAnalysis():
    url = "http://localhost:8001/analyze"
    data = {"service_name": "sentiment-analysis", "text": "This is a test text."}
    response = requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert "result" in response.json()

def test_wordCount():
    url = "http://localhost:8002/count"
    data = {"service_name": "word-count", "text": "This is a test text."}
    response = requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert "result" in response.json()

def test_entityRecognition():
    url = "http://localhost:8003/recognize"
    data = {"service_name": "entity-recognition", "text": "This is a test text."}
    response = requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert "result" in response.json()

def test_non_existent_service():
    url = f"{BASE_URL}/analyze"
    data = {"service": "non-existent-service", "text": "The weather is great today!"}
    response = requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 404
    assert "error" in response.json()