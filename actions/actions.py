# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

# bhai ye line 30 nkaise bhool gaye tum , ye toh zaroori hai 

import imp
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_show_time"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text=f"{dt.datetime.now()}")

#         return []



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"    #------> name to refer to story , domain , rule ...

    def run(self, dispatcher: CollectingDispatcher,    #------> send messages back to the user
            tracker: Tracker,     #------>  Fetch information ,  Intent, Entities, Conversation sofar
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:    #------> data defines in domain.yml files
                            
        dispatcher.utter_message(text="Hello World!")

        return []


# from typing import Any,Text, Dict, List


# import datetime as dt 
# import arrow
# import dateparser
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_tell_time"    #------> name to refer to story , domain , rule ...

#     def run(self, dispatcher: CollectingDispatcher,    #------> send messages back to the user
#             tracker: Tracker,     #------>  Fetch information ,  Intent, Entities, Conversation sofar
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:    #------> data defines in domain.yml files

#         current_place = next(tracker.get_latest_entity_values("place"),None)
#         utc = arrow.utcnow()

#     if not current_place:
#         msg = f"It's{'HH:mm'}} utc now. You can also give me a place."
#         dispatcher.utter_message(text=text=msg)

#         return []
