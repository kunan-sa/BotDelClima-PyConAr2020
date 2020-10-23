## greeting
* greet
  - utter_greet

## ask weather happy path
* ask_weather
  - action_ask_weather
  - utter_did_that_help
* affirm
  - utter_happy

## ask weather sad path
* ask_weather
  - action_ask_weather
  - utter_did_that_help
* deny
  - utter_goodbye

## say thanks
* mood_great
  - utter_denada

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
