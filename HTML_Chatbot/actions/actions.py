# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

import rasa.core.tracker_store
from rasa.shared.core.trackers import DialogueStateTracker
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSaveConversation(Action):

    def name(self) -> Text:
        return "ActionSaveConversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conversation=tracker.events
        print(conversation)
        import os
        if not os.path.isfile('chats.txt'):
            with open('chats.txt','w') as file:
                file.write("user input;bot reply"+"\n\n")
        chat_data=''
        for i in conversation:
            if i['event'] == 'user':
                chat_data+=i['text']+';'
                print('user: '+(i['text']))

            elif i['event'] == 'bot':
                print('Bot: '+(i['text']))
                try:
                    chat_data+=i['text']+'\n'
                except KeyError:
                    pass
        else:
            with open('chats.txt','a') as file:
                file.write(chat_data)
                
        return []