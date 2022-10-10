import requests

# api-endpoint
URL = "http://127.0.0.1:8648/sum"

# location given here
a = "2"
b = "3"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'a':a, 'b':b}

# sending get request and saving the response as response object
r = requests.post(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()

# printing the output
print(r)
print(data)