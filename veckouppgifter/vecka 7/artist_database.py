import requests
import json

API_URL = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

# fetches and returns a list with artist dictionaries from the API without argument
def fetch_api():
    global api_data
    api_data = requests.get(API_URL)
    status_check()
    fetched_artists = json.loads(api_data.text)["artists"]
    return fetched_artists

# raises an error if the API request failed (error) without argument
def status_check():
    if not (200 <= api_data.status_code < 300):
        raise Exception('ERROR: API request failed')

# returns a list of available artists names (strings) without argument
def list_artists():
    artists = fetch_api()
    artist_list = []
    for artist in artists:
        artist_list.append(artist['name'])
    return artist_list

# returns a dictionary of artist specifications using an artist id (string) as argument
def get_artist_by_id(artist_id):
    artists = fetch_api()
    for artist in artists:
        if artist['id'] == artist_id:
            api_data_artist = requests.get(API_URL + artist["id"])
            artist_data = json.loads(api_data_artist.text)["artist"]
            return artist_data

# returns a dictionary of artist specifications using an artist name (string) as argument
def get_artist(artist_name):
    artists = fetch_api()
    for artist in artists:
        if artist['name'] == artist_name:
            api_data_artist = requests.get(API_URL + artist["id"])
            artist_data = json.loads(api_data_artist.text)["artist"]
            return artist_data