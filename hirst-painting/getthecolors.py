import colorgram

colors = colorgram.extract('hirstspotpainting.jpg', 34)

# returns something like:
# [
# <colorgram.py Color: Rgb(r=254, g=253, b=251), 56.60501849445166%>,
# <colorgram.py Color: Rgb(r=239, g=254, b=247), 14.539638108567429%>
# ]
# print(colors)

# returns something like: Rgb(r=254, g=253, b=251)
# print(colors[0].rgb)

# returns somthing like: 254
# print(colors[0].rgb.r)


rgb_colors = []
for i in colors:
    # Create Tuple
    rgb_color = (i.rgb.r, i.rgb.g, i.rgb.b)
    rgb_colors.append(rgb_color)



print(rgb_colors)