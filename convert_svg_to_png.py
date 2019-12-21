import wand.color
import wand.image
from wand.api import library


def rasterise(source: str, target: str):
    print("""
CONVERTING SVG at   %s
                   |   |
                   |   |
                   |   |
                   |   |
                   |   |
                 __!   !__,
                 \       / \O
                  \     / \/|
                   \   /    |
                    \ /    / \ 
                     Y   _/  _\ 
        to PNG at   %s
    """ % (source, target))
    with wand.image.Image() as image:
        with wand.color.Color('transparent') as background_color:
            library.MagickSetBackgroundColor(image.wand,
                                             background_color.resource)
        with open(source, "r")as sourceFile:
            image.read(blob=sourceFile.read(), format="svg")

        png_image = image.make_blob("png32")

    with open(target, "wb") as out:
        out.write(png_image)
