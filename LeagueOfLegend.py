import requests

api_key = open("credential_riot.txt", "r").readline()
sohwan = (
    "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    + "hide on bush"
    + "?api_key="
    + api_key
)
r = requests.get(sohwan)
r.json()["id"]
