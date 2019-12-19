def numberOfTXT_inInput() -> int:
    return 0


# noinspection PyBroadException
try:
    txtFiles: int = numberOfTXT_inInput()
except:
    print("something went wrong when trying to access the 'TUMSpeak_InputFiles' - Folder")
    txtFiles: int = 0

if txtFiles > 0:
    print("Input-Source is the 'TUMSpeak_InputFiles' - Folder\n\t('TUMSpeak_InputFiles' - Folder has %d .txt Files",
          txtFiles)

else:
    print("Input-Source is the commandline\n\t('TUMSpeak_InputFiles' - Folder has %d .txt Files", txtFiles)
