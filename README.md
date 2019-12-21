# TUMSpeak
This is a very short converter frrom Text to TUMSpeak - A SVG-Based Font in the TUM-Logo Layout

## Samples

## Usage:
### Generating SVG's
__generating SVGs is eazy__, but there are two notable ways of interfacing with this Project:
- *"I want to convert a `.txt`-File"*
  - Just Put the File you want to convert in the `TUMSpeak_InputFiles`-Folder
  - add more than one File to convert more
- *"I just want this short Text converted to TUMSpeak"*
  - dont bother with creating a `.txt`-File.
  - if there are no `.txt`-File, this Programm will spawn an input Promt, to ask for the input

If an __Error message__ appears and you __DON'T want a `.png`-File__, everything __worked as expected__. Dont worry

The Results of the conversion will appear in the `TUMSpeak_OutputFiles/SVG/`-Folder

### Generating PNG's
__generating PNGs is not that hard__, but you need to follow this guide:\
Converting an SVGs is something I am not that familiar with.
This is why I got some help by the __*[Wand package](http://docs.wand-py.org/en/0.4.1/index.html)*__.

Depending on your Operating System, choose the corresponding section under
http://docs.wand-py.org/en/0.4.1/guide/install.html.
after complying with the install you should be golden, and the the __Error-Message should disapear__

The Results of the conversion will appear in the `TUMSpeak_OutputFiles/PNG/`-Folder
