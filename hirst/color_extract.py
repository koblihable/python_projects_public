from colorgram import colorgram

colors = colorgram.extract('hirst_painting.jpg', 15)

color_list = []
for color in colors:
    (r,g,b) = color.rgb
    color_list.append((r,g,b))