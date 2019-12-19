import datetime
import os
import time


def generate_new_filepath() -> str:
    time.sleep(1)
    path = os.path.dirname(__file__) + "/TUMSpeak_OutputFiles/" + datetime.datetime.now().strftime(
        "%d-%m-%Y  %Hh %Mm %Ss") + ".svg"
    print("Path: ", path)
    open(path, "x").close()
    return path


def process(text: str):
    text = text.upper().strip()
    print("Processing:\n%s" % text)
    output_path = generate_new_filepath()
    with open(output_path, "w") as o:
        o.write(text)
