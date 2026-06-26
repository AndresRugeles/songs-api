import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api = "https://songs-api-km16.onrender.com"

# GET
def get_songs():
    response = requests.get(f"{api}/songs", verify=False)
    print(f"GET status:", response.status_code)
    print(response.json())
    print(response.text)
    print(response.headers)

# POST
def create_song():
    data = {
        "artist": "Test Song",
        "title": "Tester"
    }
    response = requests.post(f"{api}/songs", json=data, verify=False)
    print(f"POST status:", response.status_code)
    print(response.json())

# PUT
def update_song(index):
    data = {
        "artist": "Updated Song",
        "title": "Tester"
    }
    response = requests.put(f"{api}/songs/{index}", json=data, verify=False)  
    print("PUT status:", response.status_code)
    print(response.json())


# DELETE
def delete_song(index):
    response = requests.delete(f"{api}/songs/{index}", verify=False)
    print("DELETE status:", response.status_code)
    print(response.json())

# FILTER - PARAMS
def filter_params(index):
    response = requests.get(f"{api}/songs/{index}")
    print(response.url)
    print(response.text)




#get_songs()
#create_song()
#update_song(0)
#delete_song()