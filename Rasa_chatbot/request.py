import requests

r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": "Socket"})