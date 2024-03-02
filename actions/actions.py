# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
#from packaging.version import parse as parse_version
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



import requests


class ActionFindflower(Action):

    def name(self) -> Text:
        return "action_Find_flowers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("flowers")
        dispatcher.utter_message(text = name)
        flower_flag =True


        # if name in flower_text:
        #     dispatcher.utter_message(text="TRUE")
        while flower_flag:
            # 检查请求是否成功
            response = requests.get('http://127.0.0.1:5001/get_text')
            if response.status_code == 200:
                # 获取实时数据
                flowertext = response.text
                # 处理接收到的实时数据
                if name in flowertext:
                    dispatcher.utter_message(text = "find it!")
                    flower_flag = False
                    return []
            else:
                print('Failed to get text:', response.status_code)
                return []



