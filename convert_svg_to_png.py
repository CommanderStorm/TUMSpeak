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

    with open(source, "r")as f:
        sourceFile = f.read().encode('utf-8')
    with wand.image.Image(blob=sourceFile, format="svg") as image:
        with wand.color.Color('transparent') as background_color:
            library.MagickSetBackgroundColor(image.wand,
                                             background_color.resource)
            image.read()

        png_image = image.make_blob("png32")

    with open(target, "wb") as out:
        out.write(png_image)
