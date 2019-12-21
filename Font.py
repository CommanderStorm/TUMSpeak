characterWidth = {
    "A": 40,
    "B": 40,
    "C": 40,
    "D": 40,
    "E": 40,
    "F": 40,
    "G": 40,
    "H": 40,
    "I": 60,
    "J": 40,
    "K": 40,
    "L": 40,
    "M": 100,
    "N": 40,
    "O": 80,
    "P": 40,
    "Q": 80,
    "R": 40,
    "S": 40,
    "T": 80,
    "U": 40,
    "V": 80,
    "W": 100,
    "X": 40,
    "Y": 80,
    "Z": 40,
    ",": 40,
    ".": 40,
    "!": 40,
    " ": 40
}


def get_character_width(character: str) -> int:
    if character in characterWidth:
        return characterWidth[character]
    return 0


def generate_svg_code(character: str) -> str:
    if not character in characterWidth or character == " ":
        return "\n"
    if character == "A":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="40" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="10" y="0" width="40" height="20" style="fill:#3070b3;"/>
            <rect x="10" y="45" width="40" height="20" style="fill:#3070b3;"/>
"""
    if character == "B":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="40" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="10" y="0" width="40" height="20" style="fill:#3070b3;"/>
            <rect x="10" y="45" width="40" height="20" style="fill:#3070b3;"/>
            <rect x="10" y="100" width="40" height="20" style="fill:#3070b3;"/>
"""
    if character == "C":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="60" height="20" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="60" height="20" style="fill:#3070b3;"/>
"""
    if character == "D":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <path d="M10,0 l30,0 l20,20 l0,80 l-20,20 l-30,0 l0,-20 l20,0 l10,-10 l0,-60 l-10,-10 l-30,0 Z"
                  style="fill:#3070b3;"/>
"""
    if character == "E":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="60" height="20" style="fill:#3070b3;"/>
            <rect x="0" y="45" width="30" height="20" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="60" height="20" style="fill:#3070b3;"/>
"""
    if character == "F":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="60" height="20" style="fill:#3070b3;"/>
            <rect x="0" y="45" width="30" height="20" style="fill:#3070b3;"/>
"""
    if character == "G":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="60" height="20" style="fill:#3070b3;"/>
            <rect x="30" y="45" width="30" height="20" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="60" height="20" style="fill:#3070b3;"/>
            <rect x="40" y="45" width="20" height="65" style="fill:#3070b3;"/>
"""
    if character == "H":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="40" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="45" width="60" height="20" style="fill:#3070b3;"/>
"""
    if character == "I":
        return """
            <rect x="25" y="0" width="30" height="20" style="fill:#3070b3;"/>
            <rect x="30" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="80" height="20" style="fill:#3070b3;"/>
"""
    if character == "J":
        return """
            <rect x="0" y="0" width="60" height="20" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="60" height="20" style="fill:#3070b3;"/>
            <rect x="40" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="80" width="20" height="40" style="fill:#3070b3;"/>
"""
    if character == "K":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <path d="M0,60 L40,0 l20,0 L20,60 L60,120 l-20,0 Z"
                  style="fill:#3070b3;"/>
"""
    if character == "L":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="60" height="20" style="fill:#3070b3;"/>
"""
    if character == "M":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="50" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="100" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="120" height="20" style="fill:#3070b3;"/>
"""
    if character == "N":
        return """
            <rect x="40" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <path d="M20,0 L60,120 l-20,0 L0,0 Z"
                  style="fill:#3070b3;"/>
"""
    if character == "O":
        return """
            <rect x="80" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="100" height="20" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="100" height="20" style="fill:#3070b3;"/>
"""
    if character == "P":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <path d="M10,0 l30,0 l20,20 l0,25 l-20,20 l-30,0 l0,-20 l20,0 l10,-10 l0,-5 l-10,-10 l-30,0 Z"
                  style="fill:#3070b3;"/>
"""
    if character == "Q":
        return """
            <rect x="80" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="100" height="20" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="100" height="20" style="fill:#3070b3;"/>
            <path d="M112.5,122.5 L102.5,132.5 L62.5,92.5 L72.5,83.5 Z"
                  style="fill:#3070b3;"/>
"""
    if character == "R":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <path d="M10,0 l30,0 l20,20 l0,25 l-20,20 l-30,0 l0,-20 l20,0 l10,-10 l0,-5 l-10,-10 l-30,0 Z"
                  style="fill:#3070b3;"/>
            <path d="M0,60 L20,60 L60,120 l-20,0 Z"
                  style="fill:#3070b3;"/>
"""
    if character == "S":
        return """
        <rect x="0" y="0" width="60" height="20" style="fill:#3070b3;"/>
        <rect x="0" y="0" width="20" height="50" style="fill:#3070b3;"/>
        <rect x="0" y="45" width="60" height="20" style="fill:#3070b3;"/>
        <rect x="40" y="50" width="20" height="60" style="fill:#3070b3;"/>
        <rect x="0" y="100" width="60" height="20" style="fill:#3070b3;"/>
"""
    if character == "T":
        return """
            <rect x="40" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="100" height="20" style="fill:#3070b3;"/>
"""
    if character == "U":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="40" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="60" height="20" style="fill:#3070b3;"/>
"""
    if character == "V":
        return """
            <path d="M20,0 l-20,0 L40,120 l20,0 L100,0 l-20,0 L50,90 Z"
                  style="fill:#3070b3;"/>
"""
    if character == "W":
        return """
            <path d="M20,0 l-20,0 L20,120 l20,0 L70,0 l-20,0 L30,80 Z"
                  style="fill:#3070b3;"/>
            <path d="M70,0 l-20,0 L80,120 l20,0 L120,0 l-20,0 L90,80 Z"
                  style="fill:#3070b3;"/>
"""
    if character == "X":
        return """
            <path d="M0,0 l20,0 L60,120 l-20,0Z"
                  style="fill:#3070b3;"/>
            <path d="M0,120 l20,0 L60,0 l-20,0Z"
                  style="fill:#3070b3;"/>
"""
    if character == "Y":
        return """
            <rect x="40" y="45" width="20" height="75" style="fill:#3070b3;"/>
            <path d="M20,0 l-20,0 L40,60 l20,0 L100,0 l-20,0 L50,45 Z"
                      style="fill:#3070b3;"/>
"""
    if character == "Z":
        return """
        <rect x="0" y="0" width="60" height="20" style="fill:#3070b3;"/>
        <rect x="0" y="100" width="60" height="20" style="fill:#3070b3;"/>
        <path d="M60,20 L20,100 l-10,10 L0,100 L40,20 l10,-10 Z"
                      style="fill:#3070b3;"/>
"""
    if character == ",":
        return """
            <rect x="10" y="110" width="10" height="40" style="fill:#3070b3;"/>
"""
    if character == ".":
        return """
            <rect x="10" y="110" width="10" height="10" style="fill:#3070b3;"/>
"""
    if character == "!":
        return """
            <rect x="10" y="110" width="10" height="10" style="fill:#3070b3;"/>
            <rect x="10" y="0" width="10" height="100" style="fill:#3070b3;"/>
"""
