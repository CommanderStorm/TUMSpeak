import datetime
import os
import time

import Font


def generate_new_filepath() -> str:
    time.sleep(1)
    path = os.path.dirname(__file__) + "/TUMSpeak_OutputFiles/" + datetime.datetime.now().strftime(
        "%d-%m-%Y  %Hh %Mm %Ss") + ".svg"
    print("Path: ", path)
    open(path, "x").close()
    return path


def processLine(i: str, xHeight: int, yHeight: int) -> str:
    out = ""
    for character in i:
        out += Font.generate_svg_code(character, xHeight, yHeight)
        xHeight += Font.get_character_width(character)
    return out


def process(text: str):
    text = text.upper().strip()
    print("Processing:\n%s" % text)
    output_path = generate_new_filepath()
    with open(output_path, "w") as o:
        xHeight, yHeight = 0, 0
        for i in text.split("\n"):
            o.write(processLine(i, xHeight, yHeight))
            xHeight = 0
            yHeight += 200
