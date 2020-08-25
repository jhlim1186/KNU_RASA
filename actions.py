# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

import quiz

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class Actionfindname(Action):

    def name(self) -> Text:
        return "Action_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name_entity = tracker.get_slot("name")
        dispatcher.utter_message("안녕하세요 {}님 반갑습니다.".format(name_entity))

        return name_entity

class ActionQuiz(Action):
    
    def name(self) -> Text:
        return "Action_Quiz"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global number 
        number = quiz.GetQuiz()
        problem  = quiz.Getproblem(number)

        dispatcher.utter_message(problem)

        return []

class ActionAnswer(Action):
    
    def name(self) -> Text:
        return "Action_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        answer  = quiz.Getanswer(number)
        answer_entity = tracker.get_slot("answer")
        
        if(answer == answer_entity):
            dispatcher.utter_message("정답은" + answer + "입니다!\n 축하드려요!")
        else:
            dispatcher.utter_message("정답은" + answer + "입니다!\n 다음엔 좀더 잘해보아요!")

        

        return []