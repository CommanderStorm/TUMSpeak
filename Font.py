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
        return """
        <g id="A" >
                <rect x="0" y="5.123" width="166.667" height="1000" style="fill:#3070b3;"/>
                <path d="M83.333,5.123l0,166.667l333.334,0l0,-166.667l-333.334,0Z" style="fill:#3070b3;"/>
                <path d="M35.417,421.79l0,166.667l417.708,0l0,-166.667l-417.708,0Z" style="fill:#3070b3;"/>
                <rect x="333.333" y="5.123" width="166.667" height="1000" style="fill:#3070b3;"/>
            </g>
        """
    if character == "B":
        return """
        <g id="B" >
                <rect x="666.667" y="5.123" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="1000" y="5.123" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="751.836" y="380.123" width="295.777" height="166.667" style="fill:#3070b3;"/>
                <rect x="760.754" y="5.123" width="308.379" height="166.667" style="fill:#3070b3;"/>
                <rect x="760.754" y="838.457" width="308.379" height="166.667" style="fill:#3070b3;"/>
            </g>
        """
    if character == "C":
        return """
        <g id="C" >
                <rect x="1333.33" y="5.123" width="500" height="166.667" style="fill:#3070b3;"/>
                <rect x="1333.33" y="838.457" width="500" height="166.667" style="fill:#3070b3;"/>
                <rect x="1333.33" y="5.123" width="166.667" height="1000" style="fill:#3070b3;"/>
            </g>
        """
    if character == "D":
        return """
        <g id="D" >
                <rect x="2000" y="5.123" width="166.667" height="1000" style="fill:#3070b3;"/>
                <path d="M2364.03,5.123l-219.882,0l0,166.667l116.163,0l103.719,83.333l0,500l-103.719,82.635l-116.163,0.699l0,166.666l219.882,0l179.313,-166.666l0,-666.667l-179.313,-166.667Z"
                      style="fill:#3070b3;"/>
            </g>
        """
    if character == "E":
        return """
        <g id="E" >
                <rect x="2685.42" y="5.123" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="2770.59" y="380.123" width="187.206" height="166.667" style="fill:#3070b3;"/>
                <rect x="2779.5" y="5.123" width="285.59" height="166.667" style="fill:#3070b3;"/>
                <rect x="2779.5" y="838.457" width="308.379" height="166.667" style="fill:#3070b3;"/>
            </g>
        """
    if character == "F":
        return """
        <g id="F" >
                <rect x="3175.52" y="5.123" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="3260.69" y="380.123" width="187.206" height="166.667" style="fill:#3070b3;"/>
                <rect x="3269.61" y="5.123" width="285.59" height="166.667" style="fill:#3070b3;"/>
            </g>
        """
    if character == "G":
        return """
        <g id="G">
                <rect x="3666.67" y="0" width="500" height="166.667" style="fill:#3070b3;"/>
                <rect x="3666.67" y="838.457" width="500" height="166.667" style="fill:#3070b3;"/>
                <rect x="3930" y="380.123" width="236.667" height="166.667" style="fill:#3070b3;"/>
                <rect x="3666.67" y="5.123" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="4000" y="515.138" width="166.667" height="489.986" style="fill:#3070b3;"/>
            </g>
        """
    if character == "H":
        return """
        <g id="H" >
                <rect x="0" y="1255.12" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="351.227" y="1255.12" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="83.333" y="1630.12" width="333.333" height="166.667" style="fill:#3070b3;"/>
            </g>
        """
    if character == "I":
        return """
        <g id="I" >
                <rect x="750" y="1255.12" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="583.333" y="2099.93" width="500" height="166.667" style="fill:#3070b3;"/>
                <rect x="666.667" y="1255.12" width="333.333" height="166.667" style="fill:#3070b3;"/>
            </g>
        """
    if character == "J":
        return """<g id="J" >
                <rect x="1499.9" y="1254.99" width="166.768" height="1000.26" style="fill:#3070b3;"/>
                <rect x="1166.67" y="2088.41" width="500" height="166.711" style="fill:#3070b3;"/>
                <path d="M1333.34,1838.46l-166.667,0l-0.001,416.666l166.666,0l0.002,-416.666Z" style="fill:#3070b3;"/>
                <rect x="1333.33" y="1255.12" width="333.333" height="166.711" style="fill:#3070b3;"/>
            </g>"""
    if character == "K":
        return """
        <g id="K" >
                <rect x="1889.33" y="1255.12" width="166.667" height="1000" style="fill:#3070b3;"/>
                <path d="M2056,1626.06l-166.667,0l342.959,629.059l166.667,0l-342.959,-629.059Z" style="fill:#3070b3;"/>
                <path d="M2108.09,1754.18l-166.667,0l290.865,-499.058l166.667,0l-290.865,499.058Z"
                      style="fill:#3070b3;"/>
            </g>
        """
    if character == "L":
        return """
        <g id="L">
                <rect x="2569.42" y="1251.4" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="2569.42" y="2084.74" width="500" height="166.667" style="fill:#3070b3;"/>
            </g>"""
    if character == "M":
        return """
        <g id="M" >
                <rect x="0" y="2500" width="166.667" height="1000" style="fill:#3070b3;"/>
                <path d="M83.333,2500l0,166.667l864.188,0l0,-166.667l-864.188,0Z" style="fill:#3070b3;"/>
                <rect x="416.667" y="2500" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="833.333" y="2500" width="166.667" height="1000" style="fill:#3070b3;"/>
            </g>"""
    if character == "N":
        return """
        <g id="N" >
                <rect x="1256.79" y="2505.12" width="166.667" height="1000" style="fill:#3070b3;"/>
                <path d="M1423.45,2505.12l-153.595,64.703l406.323,935.297l153.595,-64.702l-406.323,-935.298Z"
                      style="fill:#3070b3;"/>
                <rect x="1676.18" y="2505.12" width="166.667" height="1000" style="fill:#3070b3;"/>
            </g>
        """
    if character == "O":
        return """
        <g id="O">
                <path d="M3018.74,3500.14l-833.333,0l0,-1000.14l833.333,0l0,1000.14Zm-666.666,-833.469l0,666.802l500,0l0,-666.802l-500,0Z"
                      style="fill:#3070b3;"/>
            </g>
        """
    if character == "P":
        return """
        <g id="P">
                <rect x="3250.83" y="2500" width="166.667" height="1000" style="fill:#3070b3;"/>
                <path d="M3583.33,2500l-204.375,0l0,166.667l121.042,0l83.333,83.333l0,83.333l-83.333,82.635l-121.042,0.699l0,166.666l204.375,0l166.667,-166.666l0,-250l-166.667,-166.667Z"
                      style="fill:#3070b3;"/>
            </g>
        """
    if character == "Q":
        return """<g id="Q">
                <path d="M833.333,4829.11l-833.333,0l0,-1000.14l833.333,0l0,1000.14Zm-666.666,-833.469l0,666.802l500,0l0,-666.802l-500,0Z"
                      style="fill:#3070b3;"/>
                <path d="M563.768,4483.18l-112.782,112.782l377.153,377.154l112.783,-112.782l-377.154,-377.154Z"
                      style="fill:#3070b3;"/>
            </g>"""
    if character == "R":
        return """
        <g id="R">
                <path d="M1224.94,4385.49l166.667,0l284.576,443.486l-166.666,0l-284.577,-443.486Z"
                      style="fill:#3070b3;"/>
                <path d="M1496.87,3828.97l-219.882,0l0,166.667l130.226,0l89.656,83.333l0,83.334l-89.656,82.634l-130.226,0.699l0,166.667l219.882,0l179.312,-166.667l0,-250l-179.312,-166.667Z"
                      style="fill:#3070b3;"/>
                <rect x="1138.47" y="3828.97" width="166.667" height="1000" style="fill:#3070b3;"/>
            </g>
        """
    if character == "S":
        return """
        <g id="S">
                <rect x="1833.33" y="4662.31" width="500" height="166.667" style="fill:#3070b3;"/>
                <rect x="1833.33" y="3831.53" width="500" height="166.667" style="fill:#3070b3;"/>
                <rect x="1835.88" y="3938.91" width="166.667" height="388.256" style="fill:#3070b3;"/>
                <rect x="1833.33" y="4245.3" width="500" height="166.667" style="fill:#3070b3;"/>
                <rect x="2166.67" y="4273.4" width="166.667" height="547.352" style="fill:#3070b3;"/>
            </g>
        """
    if character == "T":
        return """
        <g id="T">
                <rect x="2790.51" y="3827.17" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="2540.51" y="3827.17" width="666.667" height="166.667" style="fill:#3070b3;"/>
            </g>
        """
    if character == "U":
        return """
        <g id="U">
                <rect x="3750.83" y="3827.17" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="3417.5" y="3827.17" width="166.667" height="1000" style="fill:#3070b3;"/>
                <rect x="3417.5" y="4660.5" width="500" height="166.667" style="fill:#3070b3;"/>
            </g>
        """
    if character == "V":
        return """
        <g id="V">
                <path d="M883.333,5234.73l-166.715,0l-342.119,1000l166.715,0l342.119,-1000Z" style="fill:#3070b3;"/>
                <path d="M166.715,5234.73l-166.715,0l342.119,1000l166.715,0l-342.119,-1000Z" style="fill:#3070b3;"/>
            </g>
        """
    if character == "W":
        return """
        <g id="W">
                <g id="Ebene92">
                    <path d="M1586.57,5234.73l-172.205,0l-196.437,1000l172.204,0l196.438,-1000Z" style="fill:#3070b3;"/>
                    <path d="M1174.76,5234.73l-172.205,0l196.438,1000l172.205,0l-196.438,-1000Z" style="fill:#3070b3;"/>
                </g>
                <g id="Ebene93">
                    <path d="M2002.55,5234.73l-172.204,0l-196.438,1000l172.205,0l196.437,-1000Z" style="fill:#3070b3;"/>
                    <path d="M1590.74,5234.73l-172.204,0l196.437,1000l172.205,0l-196.438,-1000Z" style="fill:#3070b3;"/>
                </g>
            </g>
        """
    if character == "X":
        return """
        <g id="X">
                <path d="M2240.72,5234.73l-157.392,0l328.696,1000l157.391,0l-328.695,-1000Z" style="fill:#3070b3;"/>
                <path d="M2583.33,5234.73l-157.391,0l-328.695,1000l157.391,0l328.695,-1000Z" style="fill:#3070b3;"/>
            </g>
        """
    if character == "Y":
        return """
        <g id="Y">
                <path d="M3489.58,5234.73l-166.667,0l-291.667,411.158l166.667,0l291.667,-411.158Z"
                      style="fill:#3070b3;"/>
                <path d="M2739.58,5234.73l166.666,0l291.667,411.158l-166.667,0l-291.666,-411.158Z"
                      style="fill:#3070b3;"/>
                <rect x="3031.25" y="5623.57" width="166.667" height="611.158" style="fill:#3070b3;"/>
            </g>
        """
    if character == "Z":
        return """
        <g id="Z">
                <path d="M4069.53,5234.73l-499.999,-0.846l-0.282,166.666l499.999,0.847l0.282,-166.667Z"
                      style="fill:#3070b3;"/>
                <path d="M4069.27,5401.33l-117.652,-118.051l-383.493,783.952l117.652,118.05l383.493,-783.951Z"
                      style="fill:#3070b3;"/>
                <path d="M4068.12,6068.07l-499.999,-0.846l-0.282,166.666l499.999,0.847l0.282,-166.667Z"
                      style="fill:#3070b3;"/>
            </g>
        """
    if character == ",":
        return """
        <g id=",">
                <rect x="553.502" y="7234.29" width="83.333" height="241.463" style="fill:#3070b3;"/>
            </g>
        """
    if character == ".":
        return """
        <g id=".">
                <rect x="252.616" y="7234.29" width="83.333" height="83.333" style="fill:#3070b3;"/>
            </g>
        """
    if character == "!":
        return """
        <g id="!">
                <rect x="937.783" y="6329.3" width="83.333" height="833.333" style="fill:#3070b3;"/>
                <rect x="937.783" y="7234.29" width="83.333" height="83.333" style="fill:#3070b3;"/>
            </g>
        """
