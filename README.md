# web-dashboard-virtual-agent
Example of how we can integrate virtual agents in a R Shiny web-dashboard.


## How to use it

1 - The first step is to run rasa with the following lines in two different cmd: 
- rasa run actions
- rasa run --model models --enable-api --cors "*"

2 - Run the app.R file (and change at line 42 the path of the index.html file)
3 - Send the message "socket" to activate the socket communication via the widget or with the POST request by running the request.py file

NOTE: if the widget does not appear on the dashboard, it is possible to use the chatbot rasa by running the index.html file with google chrome locally.
