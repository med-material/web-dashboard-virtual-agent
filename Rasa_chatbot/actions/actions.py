from rasa.core.actions.action import Action
import datetime as dt 
from typing import Any, Text, Dict, List
import socket
from rasa_sdk import Action, Tracker, events
from rasa_sdk.executor import CollectingDispatcher
from rasa.core.channels.channel import InputChannel

class CreateSocket(Action):
    def name(self) -> Text:
        return "CreateSocket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # créer la socket
        CreateSocket.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # se connecte au server
        CreateSocket.s.connect(("localhost", 5006))

        return []

class SendSummaryAction(Action):
    def name(self) -> Text:
        return "SendSummaryAction"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        CreateSocket.s.send(b'summary')

        return []

class SendPlotAction(Action):
    def name(self) -> Text:
        return "SendPlotAction"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        CreateSocket.s.send(b'plot')

        return []

class SendTableAction(Action):
    def name(self) -> Text:
        return "SendTableAction"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        CreateSocket.s.send(b'table')

        return []