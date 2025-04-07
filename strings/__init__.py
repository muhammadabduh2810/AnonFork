#
# Copyright (C) 2021-2022 by DemusIndonesia@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @MusicIndoListening
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alisha © Alexa © Yukki


import os
from typing import List

import yaml

languages = {}
commands = {}


def get_command(value: str) -> List:
    return commands["command"][value]


def get_string(lang: str):
    return languages[lang]


for filename in os.listdir(r"./strings"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        commands[language_name] = yaml.safe_load(
            open(r"./strings/" + filename, encoding="utf8")
        )


for filename in os.listdir(r"./strings/langs/"):
    if "en" not in languages:
        languages["indonesia"] = yaml.safe_load(
            open(r"./strings/langs/en.yml", encoding="utf8")
        )
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "indonesia":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["indonesia"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["indonesia"][item]
