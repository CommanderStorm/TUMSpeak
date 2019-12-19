import datetime
import os


def generateNewFilepath() -> str:
    path = os.path.dirname(__file__) + "/TUMSpeak_OutputFiles/" + datetime.datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S') + ".svg"
    print("Path: ", path)
    open(path, "x")
    return path


def process(text: str):
    text = text.upper().strip()
    print("Processing:\n%s" % text)
    outputfilePath = generateNewFilepath()
    # possible file collision, but my computer is to slow for such an event to occur
    with open(outputfilePath) as o:
        o.write("hi")
