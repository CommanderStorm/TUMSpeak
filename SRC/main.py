import glob

import SRC.processor as pro

inputPath = ""


def number_of_txt_in_input() -> int:
    return len(glob.glob1(inputPath, "*.tif"))


# noinspection PyBroadException
try:
    txtFiles: int = number_of_txt_in_input()
except:
    print("something went wrong when trying to access the 'TUMSpeak_InputFiles' - Folder")
    txtFiles: int = 0

if txtFiles > 0:
    print("Input-Source is the 'TUMSpeak_InputFiles' - Folder")
    print("('TUMSpeak_InputFiles' - Folder has %d .txt Files)\n" % txtFiles)
    # for (i in filenames):
    #    pro.process(i)

else:
    print("Input-Source is the commandline")
    print("('TUMSpeak_InputFiles' - Folder has %d .txt Files)" % txtFiles)
    textToBeConverted = input("Please input the Text, you would like to have converted to TUMSpeak\n\t>")
    pro.process(textToBeConverted)
