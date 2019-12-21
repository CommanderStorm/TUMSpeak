import datetime
import os
import time

import Font
import convert_svg_to_png as convert

x_height = 0
y_height = 0
filename = ""


def generate_new_filepath() -> str:
    global filename
    time.sleep(1)
    filename = "TUMSpeak" + datetime.datetime.now().strftime("%d-%m-%Y  %Hh %Mm %Ss")
    path = os.path.dirname(__file__) + "/TUMSpeak_OutputFiles/SVG/" + filename + ".svg"
    print("Path: ", path)
    open(path, "x").close()
    return path


def process_line(i: str) -> str:
    global x_height
    out = ""
    for character in i:
        out += """\n       <g  transform="matrix(1,0,0,1,%d,%d)">""" % (x_height, y_height)
        out += Font.generate_svg_code(character)

        out += "       </g>\n"
        x_height += Font.get_character_width(character)
    return out


def is_one_liner_without_q(text: str) -> bool:
    first_line = True
    for i in text.split("\n"):
        if not first_line:
            return False
        for c in i:
            if c in ["Q", ","]:
                return False
    return True


def get_max_y(text: str) -> int:
    out = 0
    if is_one_liner_without_q(text):
        return 120
    for i in text.split("\n"):
        out += 140
    return out


def get_max_x(text: str) -> int:
    out = 20
    for i in text.split("\n"):
        line_length = 20
        for character in i:
            line_length += Font.get_character_width(character)
        if line_length > out:
            out = line_length
    return out


def process(text: str):
    global x_height, y_height
    text = text.upper().strip()
    print("Processing:\n%s" % text)
    output_path = generate_new_filepath()
    x_height = 0
    y_height = 0
    with open(output_path, "w") as o:
        o.write("""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="100%" height="100%""" + """" viewBox="0 0 %d %d" version="1.1" xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/"
     style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">
    <g>
""" % (get_max_x(text), get_max_y(text)))
        for i in text.split("\n"):
            o.write(process_line(i))
            x_height = 0
            y_height += 140
        o.write("""
    </g>
</svg>""")
    convert.rasterise(output_path, os.path.dirname(__file__) + "/TUMSpeak_OutputFiles/PNG/" + filename + ".png")
