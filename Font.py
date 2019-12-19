characterWidth = {
    "A": 60,
    "B": 60,
    "C": 60,
    "D": 60,
    "E": 60,
    "F": 60,
    "G": 60,
    "H": 60,
    "I": 60,
    "J": 60,
    "K": 60,
    "L": 60,
    "M": 120,
    "N": 60,
    "O": 120,
    "P": 60,
    "Q": 120,
    "R": 60,
    "S": 60,
    "T": 60,
    "U": 60,
    "V": 60,
    "W": 120,
    "X": 60,
    "Y": 60,
    "Z": 60,
    ",": 20,
    ".": 20,
    "!": 20
}


def get_character_width(character: str) -> int:
    if character in characterWidth:
        return characterWidth[character]
    return 0


def generate_svg_code(character: str, xHeight: int, yHeight: int) -> str:
    if not character in characterWidth:
        return ""
    if character == "A":
        return ""
    if character == "B":
        return ""
    if character == "C":
        return ""
    if character == "D":
        return ""
    if character == "E":
        return ""
    if character == "F":
        return ""
    if character == "G":
        return ""
    if character == "H":
        return ""
    if character == "I":
        return ""
    if character == "J":
        return ""
    if character == "K":
        return ""
    if character == "L":
        return ""
    if character == "M":
        return ""
    if character == "N":
        return ""
    if character == "O":
        return ""
    if character == "P":
        return ""
    if character == "Q":
        return ""
    if character == "R":
        return ""
    if character == "S":
        return ""
    if character == "T":
        return ""
    if character == "U":
        return ""
    if character == "V":
        return ""
    if character == "W":
        return ""
    if character == "X":
        return ""
    if character == "Y":
        return ""
    if character == "Z":
        return ""
    if character == ",":
        return ""
    if character == ".":
        return ""
    if character == "!":
        return ""
