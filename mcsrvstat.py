import urllib.request
import json


class ServerStatus:
    online: bool
    version: str
    motd: str
    max_players: int
    online_players: int

    def __init__(self, server_address: str):
        response = urllib.request.urlopen("https://api.mcsrvstat.us/1/%s" % server_address)
        data = json.load(response)
        self.online = data['debug']['ping']
        self.motd = data['motd']['clean'][0]
        self.version = data['version']
        self.online_players = data['players']['online']
        self.max_players = data['players']['max']
