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
    filename = datetime.datetime.now().strftime("%d-%m-%Y  %Hh %Mm %Ss")
    path = os.path.dirname(__file__) + "/TUMSpeak_OutputFiles/SVG" + filename + ".svg"
    print("Path: ", path)
    open(path, "x").close()
    return path


def process_line(i: str) -> str:
    global x_height
    out = ""
    for character in i:
        out += """\n       <g  transform="matrix(1,0,0,1,%d,%d)">\n""" % (x_height, y_height)
        out += Font.generate_svg_code(character)

        out += "\n       </g>\n"
        x_height += Font.get_character_width(character)
    return out


def process(text: str):
    global x_height, y_height
    text = text.upper().strip()
    print("Processing:\n%s" % text)
    output_path = generate_new_filepath()
    with open(output_path, "w") as o:
        o.write("""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="100%" height="100%" viewBox="0 0 2000 200" version="1.1" xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/"
     style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">
    <g>
""")
        for i in text.split("\n"):
            o.write(process_line(i))
            x_height = 0
            y_height += 200
            o.write("""
    </g>
</svg>
        """)
    convert.rasterise(output_path, os.path.dirname(__file__) + "/TUMSpeak_OutputFiles/PNG" + filename + ".png")
