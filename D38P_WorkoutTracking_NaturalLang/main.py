import requests
import datetime as dt
import os


api_key = "4559e088b5be65bdb26eeed21d7640d1"
api_id = "6626694e"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/c3fcb965379cf87aa728fed166797a3b/myWorkouts/workouts"
sheety_token = "rgesrhdfhdhdewwgw"

query = input("What kind of workout did you have today?")

now = dt.datetime.now()
date = now.date().strftime("%y/%m/%d")
time = now.time().strftime("%H:%M:%S")


header = {
    "x-app-id": api_id,
    "x-app-key": api_key
}
parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 78.5,
    "height_cm": 177.5,
    "age": 19
}

response = requests.post(url=exercise_endpoint, data=parameters, headers=header)
response.raise_for_status()
data = response.json()

exercise_list = data["exercises"]

sheety_headers = {"Authorization": "Bearer rgesrhdfhdhdewwgw"}

for i in range(len(exercise_list)):
    exercise = data["exercises"][i]["name"]
    duration = data["exercises"][i]["duration_min"]
    calories = data["exercises"][i]["nf_calories"]

    data_to_sheety = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }
    response = requests.post(url=sheety_url, json=data_to_sheety, headers=sheety_headers)
    print(response.text)

