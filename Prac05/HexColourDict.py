HEX_COLOURS = {"AntiqueWhite": "#faebd7", "Maroon": "#b03060", "Lavender": "#e6e6fa", "HotPink": "#ff69b4",
               "ForestGreen": "#228b22", "Beige": "#f5f5dc", "CornflowerBlue": "#6495ed", "GreenYellow": "#adff2f",
               "IndianRed": "#cd5c5c", "LemonChiffon1": "#fffacd"}

print("Avaliable colours:", end=" ")
for colours in sorted(HEX_COLOURS):
    print(colours, end=" ")

colour = input("\nEnter a colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print("The hex code for {} is {}".format(colour, HEX_COLOURS[colour]))
    else:
        print("Invalid colour choice state")
    colour = input("Enter a color: ")