characterWidth = {
    "A": 40,
    "B": 40,
    "C": 40,
    "D": 40,
    "E": 40,
    "F": 40,
    "G": 40,
    "H": 40,
    "I": 40,
    "J": 40,
    "K": 40,
    "L": 40,
    "M": 100,
    "N": 40,
    "O": 100,
    "P": 40,
    "Q": 100,
    "R": 40,
    "S": 40,
    "T": 60,
    "U": 40,
    "V": 40,
    "W": 100,
    "X": 40,
    "Y": 40,
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
            <rect x="10" y="40" width="40" height="20" style="fill:#3070b3;"/>
"""
    if character == "B":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="40" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="10" y="0" width="40" height="20" style="fill:#3070b3;"/>
            <rect x="10" y="40" width="40" height="20" style="fill:#3070b3;"/>
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
            <rect x="0" y="40" width="30" height="20" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="60" height="20" style="fill:#3070b3;"/>
"""
    if character == "F":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="60" height="20" style="fill:#3070b3;"/>
            <rect x="0" y="40" width="30" height="20" style="fill:#3070b3;"/>
"""
    if character == "G":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="0" width="60" height="20" style="fill:#3070b3;"/>
            <rect x="30" y="40" width="30" height="20" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="60" height="20" style="fill:#3070b3;"/>
            <rect x="40" y="40" width="20" height="60" style="fill:#3070b3;"/>
"""
    if character == "H":
        return """
            <rect x="0" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="40" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="40" width="60" height="20" style="fill:#3070b3;"/>
"""
    if character == "I":
        return """
            <rect x="10" y="0" width="40" height="120" style="fill:#3070b3;"/>
            <rect x="20" y="0" width="20" height="120" style="fill:#3070b3;"/>
            <rect x="0" y="100" width="60" height="20" style="fill:#3070b3;"/>
"""
    if character == "J":
        return """<g id="J" transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="1499.9" y="1254.99" width="20" height="10" style="fill:#3070b3;"/>
                    <rect x="1166.67" y="2088.41" width="60" height="20" style="fill:#3070b3;"/>
                    <path d="M1333.34,1838.46l-20,0l-0.001,416.666l166.666,0l0.002,-416.666Z" style="fill:#3070b3;"/>
                    <rect x="1333.33" y="1255.12" width="40" height="20" style="fill:#3070b3;"/>
                </g> """
    if character == "K":
        return """
            <g id="K" transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="1889.33" y="1255.12" width="20" height="120" style="fill:#3070b3;"/>
                    <path d="M2056,1626.06l-20,0l342.959,629.059l20,0l-342.959,-629.059Z" style="fill:#3070b3;"/>
                    <path d="M2108.09,1754.18l-20,0l290.865,-499.058l20,0l-290.865,499.058Z"
                          style="fill:#3070b3;"/>
                </g>
             """
    if character == "L":
        return """
            <g id="L" transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="2569.42" y="1251.4" width="20" height="120" style="fill:#3070b3;"/>
                    <rect x="2569.42" y="2084.74" width="60" height="20" style="fill:#3070b3;"/>
                </g> """
    if character == "M":
        return """
            <g id="M" transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="0" y="260" width="20" height="120" style="fill:#3070b3;"/>
                    <path d="M10,260l0,20l864.188,0l0,-20l-864.188,0Z" style="fill:#3070b3;"/>
                    <rect x="416.667" y="260" width="20" height="120" style="fill:#3070b3;"/>
                    <rect x="100" y="260" width="20" height="120" style="fill:#3070b3;"/>
                </g> """
    if character == "N":
        return """
            <g id="N" transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="1256.79" y="2505.12" width="20" height="120" style="fill:#3070b3;"/>
                    <path d="M1423.45,2505.12l-153.595,64.703l406.323,935.297l153.595,-64.702l-406.323,-935.298Z"
                          style="fill:#3070b3;"/>
                    <rect x="1676.18" y="2505.12" width="20" height="120" style="fill:#3070b3;"/>
                </g>
             """
    if character == "O":
        return """
            <g id="O" transform="matrix(0.12,0,0,0.12,0,0)">
                    <path d="M3018.74,360.14l-100,0l0,-120.14l100,0l0,120.14Zm-666.666,-833.469l0,666.802l60,0l0,-666.802l-60,0Z"
                          style="fill:#3070b3;"/>
                </g>
             """
    if character == "P":
        return """
            <g id="P" transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="3250.83" y="260" width="20" height="120" style="fill:#3070b3;"/>
                    <path d="M3583.33,260l-204.375,0l0,20l121.042,0l10,10l0,10l-10,82.635l-121.042,0.699l0,166.666l204.375,0l20,-166.666l0,-250l-20,-20Z"
                          style="fill:#3070b3;"/>
                </g>
             """
    if character == "Q":
        return """<g id="Q" transform="matrix(0.12,0,0,0.12,0,0)">
                    <path d="M100,4829.11l-100,0l0,-120.14l100,0l0,120.14Zm-666.666,-833.469l0,666.802l60,0l0,-666.802l-60,0Z"
                          style="fill:#3070b3;"/>
                    <path d="M563.768,4483.18l-112.782,112.782l377.153,377.154l112.783,-112.782l-377.154,-377.154Z"
                          style="fill:#3070b3;"/>
                </g> """
    if character == "R":
        return """
            <g id="R" transform="matrix(0.12,0,0,0.12,0,0)">
                    <path d="M1224.94,4385.49l20,0l284.576,443.486l-166.666,0l-284.577,-443.486Z"
                          style="fill:#3070b3;"/>
                    <path d="M1496.87,3828.97l-219.882,0l0,20l130.226,0l89.656,10l0,83.334l-89.656,82.634l-130.226,0.699l0,20l219.882,0l179.312,-20l0,-250l-179.312,-20Z"
                          style="fill:#3070b3;"/>
                    <rect x="1138.47" y="3828.97" width="20" height="120" style="fill:#3070b3;"/>
                </g>
             """
    if character == "S":
        return """
            <g id="S" transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="1833.33" y="4662.31" width="60" height="20" style="fill:#3070b3;"/>
                    <rect x="1833.33" y="3831.53" width="60" height="20" style="fill:#3070b3;"/>
                    <rect x="1835.88" y="3938.91" width="20" height="45" style="fill:#3070b3;"/>
                    <rect x="1833.33" y="4245.3" width="60" height="20" style="fill:#3070b3;"/>
                    <rect x="2166.67" y="4273.4" width="20" height="60" style="fill:#3070b3;"/>
                </g>
             """
    if character == "T":
        return """
            <g id="T" transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="2790.51" y="3827.17" width="20" height="120" style="fill:#3070b3;"/>
                    <rect x="2540.51" y="3827.17" width="80" height="20" style="fill:#3070b3;"/>
                </g>
             """
    if character == "U":
        return """
            <g id="U" transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="3750.83" y="3827.17" width="20" height="120" style="fill:#3070b3;"/>
                    <rect x="3417.5" y="3827.17" width="20" height="120" style="fill:#3070b3;"/>
                    <rect x="3417.5" y="4640.5" width="60" height="20" style="fill:#3070b3;"/>
                </g>
             """
    if character == "V":
        return """
            <g id="V" transform="matrix(0.12,0,0,0.12,0,0)">
                    <path d="M810,5234.73l-166.715,0l-342.119,120l166.715,0l342.119,-120Z" style="fill:#3070b3;"/>
                    <path d="M166.715,5234.73l-166.715,0l342.119,120l166.715,0l-342.119,-120Z" style="fill:#3070b3;"/>
                </g>
             """
    if character == "W":
        return """
            <g id="W" transform="matrix(0.12,0,0,0.12,0,0)">
                    <g id="Ebene92">
                        <path d="M1586.57,5234.73l-172.205,0l-196.437,120l172.204,0l196.438,-120Z" style="fill:#3070b3;"/>
                        <path d="M1174.76,5234.73l-172.205,0l196.438,120l172.205,0l-196.438,-120Z" style="fill:#3070b3;"/>
                    </g>
                    <g id="Ebene93">
                        <path d="M2002.55,5234.73l-172.204,0l-196.438,120l172.205,0l196.437,-120Z" style="fill:#3070b3;"/>
                        <path d="M1590.74,5234.73l-172.204,0l196.437,120l172.205,0l-196.438,-120Z" style="fill:#3070b3;"/>
                    </g>
                </g>
             """
    if character == "X":
        return """
            <g id="X" transform="matrix(0.12,0,0,0.12,0,0)">
                    <path d="M2240.72,5234.73l-157.392,0l328.696,120l157.391,0l-328.695,-120Z" style="fill:#3070b3;"/>
                    <path d="M2583.33,5234.73l-157.391,0l-328.695,120l157.391,0l328.695,-120Z" style="fill:#3070b3;"/>
                </g>
             """
    if character == "Y":
        return """
            <g id="Y" transform="matrix(0.12,0,0,0.12,0,0)">
                    <path d="M3489.58,5234.73l-20,0l-291.667,411.158l20,0l291.667,-411.158Z"
                          style="fill:#3070b3;"/>
                    <path d="M2739.58,5234.73l166.666,0l291.667,411.158l-20,0l-291.666,-411.158Z"
                          style="fill:#3070b3;"/>
                    <rect x="3031.25" y="5623.57" width="20" height="70" style="fill:#3070b3;"/>
                </g>
             """
    if character == "Z":
        return """
            <g id="Z" transform="matrix(0.12,0,0,0.12,0,0)">
                    <path d="M4069.53,5234.73l-499.999,-0.846l-0.282,166.666l499.999,0.847l0.282,-20Z"
                          style="fill:#3070b3;"/>
                    <path d="M4069.27,5401.33l-117.652,-118.051l-383.493,783.952l117.652,118.05l383.493,-783.951Z"
                          style="fill:#3070b3;"/>
                    <path d="M4068.12,4068.07l-499.999,-0.846l-0.282,166.666l499.999,0.847l0.282,-20Z"
                          style="fill:#3070b3;"/>
                </g>
             """
    if character == ",":
        return """
            <g id="," transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="553.502" y="7234.29" width="10" height="40" style="fill:#3070b3;"/>
                </g>
             """
    if character == ".":
        return """
            <g id="." transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="252.616" y="7234.29" width="10" height="10" style="fill:#3070b3;"/>
                </g>
             """
    if character == "!":
        return """
            <g id="!" transform="matrix(0.12,0,0,0.12,0,0)">
                    <rect x="937.783" y="6329.3" width="10" height="100" style="fill:#3070b3;"/>
                    <rect x="937.783" y="7234.29" width="10" height="10" style="fill:#3070b3;"/>
                </g>
             """
