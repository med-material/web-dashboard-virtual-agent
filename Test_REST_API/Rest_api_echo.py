import requests

# api-endpoint
URL = "http://127.0.0.1:8648/echo"

# location given here
msg = "Hello"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'msg':msg}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()

# printing the output
print(r)
print(data)

