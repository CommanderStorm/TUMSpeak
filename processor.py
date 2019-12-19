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


def process_line(i: str, xHeight: int, yHeight: int) -> str:
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
        o.write("""
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="100%" height="100%" viewBox="0 0 4167 8334" version="1.1" xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/"
     style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">
     <g>
        """)
        x_height, y_height = 0, 0
        for i in text.split("\n"):
            o.write(process_line(i, x_height, y_height))
            x_height = 0
            y_height += 200
        o.write("""
    </g>
</svg>
        """)
