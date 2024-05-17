import colorgram

colors = colorgram.extract("image.jpg", 30)
palette = []


def get_palette():
    for i in range(len(colors)):
        color = colors[i].rgb
        palette.append(tuple(color))
    # remove whites
    clean_palette = palette[4:]
    return clean_palette
