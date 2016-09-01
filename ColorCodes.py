COLOR_CODES = {"grey": "#bebebe", "black": "#000000", "white": "#ffffff", "yellow": "#ffff00", "red": "#ff0000",
               "blue": "#0000ff", "green": "#00ff00", "orange": "#ffa500", "pink": "#ffc0cb", "purple": "#a020f0"}

color = input("Enter color: ")
while color != "":
    if color in COLOR_CODES:
        print(color, "is", COLOR_CODES[color])
    else:
        print("Invalid color")
    color = input("Enter color")
