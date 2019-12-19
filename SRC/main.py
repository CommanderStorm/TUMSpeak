def numberOfTXT_inInput() -> int:
    return 0


try:
    txtFiles: int = numberOfTXT_inInput()
except:
    print("something went wrong when trying to access the 'TUMSpeak_InputFiles' - Folder")
    txtFiles: int = 0

if (numberOfTXT_inInput() > 0):
    print("Input-Source is the 'TUMSpeak_InputFiles' - Folder")

else:
    print("Input-Source is the commandline \n('TUMSpeak_InputFiles' - Folder has %d .txt Files", numberOfTXT_inInput())
