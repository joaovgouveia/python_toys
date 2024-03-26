import drawings_patterns as dp

def draw(drawing_name):
    if drawing_name in drawings["list"]:
        drawings[drawing_name]()
    else: print("Drawing not found!")


drawings = {
    "spiral_1": dp.spiral_1,
    "spiral_2": dp.spiral_2,
    "list": ["spiral_1", "spiral_2"]
}
