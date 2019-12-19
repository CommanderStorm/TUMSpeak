import glob
import os

import processor as pro

inputPath = os.path.dirname(__file__) + "/TUMSpeak_InputFiles"


def number_of_txt_in_input() -> int:
    return len(glob.glob1(inputPath, "*.txt"))


# noinspection PyBroadException
try:
    txtFiles: int = number_of_txt_in_input()
except:
    print("something went wrong when trying to access the 'TUMSpeak_InputFiles' - Folder")
    txtFiles: int = 0

if txtFiles > 0:
    print("\nInput-Source is the '%s' - Folder" % inputPath)
    if txtFiles > 1:
        print("('TUMSpeak_InputFiles' - Folder has %d .txt Files)" % txtFiles)
    else:
        print("('TUMSpeak_InputFiles' - Folder has 1 .txt File)")
    filecounter = 1
    for i in glob.glob1(inputPath, "*.txt"):
        print("\n-----------------------------------------"
              "\nFile #", filecounter)
        filecounter += 1
        pro.process(open(inputPath + "/" + i).read())

else:
    print("Input-Source is the commandline")
    print("('TUMSpeak_InputFiles' - Folder has %d .txt Files)" % txtFiles)
    textToBeConverted = input("Please input the Text, you would like to have converted to TUMSpeak\n\t>")
    pro.process(textToBeConverted)
