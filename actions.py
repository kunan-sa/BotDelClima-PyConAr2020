# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from api_key import API_KEY


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_ask_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # consultamos la API https://openweathermap.org/current

        city_name = tracker.get_slot('provincia')
        state_code = ''
        country_code = 'AR'
        lang = 'es'
        units = 'metric'
        
        payload = { 'q': f'{city_name},{state_code},{country_code}', 
            'appid': API_KEY,
            'lang': lang,
            'units': units
            }

        r = requests.get(
                    'http://api.openweathermap.org/data/2.5/weather',
                    params=payload
                    )
        response = r.json()

        if response.get('cod') == 200:
            T_max = response['main']['temp_max']
            T_min = response['main']['temp_min']
            weather = response['weather'][0]['description']
            message = f"Según mis investigaciones.. En {city_name}"
            message += f" tendremos clima con: {weather}. "
            message += f"Con temperatura entre {T_min} y {T_max} grados Celsius."
        else:
            message = 'Lo siento, no encontré información disponible.'
        dispatcher.utter_message(text=message)

        return []
