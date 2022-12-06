import requests
import datetime
hours = str(8)

today = datetime.datetime.now()
today = today.strftime("%Y%m%d")


pixela_endpoint = "https://pixe.la/v1/users"
token = "egywfuyq28932983hd"
username = "pratiktest610"

user_parameters = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
headers ={
    "X-USER-TOKEN": token
}
graph_cofig ={
    "id": "graph001",
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "momiji",
    "timezone": "Asia/Calcutta"
}

# response = requests.post(url=graph_endpoint, json=graph_cofig, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/graph001"
pixel_config = {
    # "date": today,
    "quantity": hours
}
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

response = requests.put(url=f"{pixel_endpoint}/20220824", json=pixel_config, headers=headers)
print(response.text)
