import os
import urllib.request
import json
import tempfile
import random
from PIL import Image, ImageFont, ImageDraw


class ServerStatus:
    __img_counter: int = 0
    font = ImageFont.truetype('./static/mcfont.ttf', 50)
    smaller_font = ImageFont.truetype('./static/mcfont.ttf', 35)
    ultra_small_font = ImageFont.truetype('./static/mcfont.ttf', 10)

    def __init__(self, server_address: str) -> None:
        response = urllib.request.urlopen("https://api.mcsrvstat.us/1/%s" % server_address)
        data = json.load(response)
        self.online: bool = data['debug']['ping']
        # If not online skip this
        if self.online:
            self.motd: str = data['motd']['clean'][0].strip()
            self.version: int = data['version']
            self.online_players: int = data['players']['online']
            self.max_players: int = data['players']['max']

    def generate_status_image(self) -> str:
        # If not online, generating status image is not possible
        img: Image = Image.open("./static/background.jpg")
        draw = ImageDraw.Draw(img)
        # Draw image
        draw.text((50, 0), self.motd, (255, 255, 255), self.font)
        draw.text(
            (50, 180),
            "{0} online  players of {1} max".format(
                self.online_players, self.max_players), (0, 255, 0), self.smaller_font
        )
        draw.text((50, 250), "Version: {0}".format(self.version), (255, 255, 0), self.smaller_font)
        draw.text((1120 - 340, 700 - 30), "Generated using Minecraft Server Status Bot [Discord]", (255, 255, 255),)
        # Generate temporary image path
        img_path = "./tmp/tmp-{0}.png".format(++self.__img_counter)
        img.save(img_path)
        return img_path

