import random

# The class gene represents a triangle

# It has 7 attributes:
# - coord_1: One of the triangle vertices
# - coord_2: One of the triangle vertices
# - coord_3: One of the triangle vertices
# - colorR: The Red color component
# - colorG: The Green color component
# - colorB: The Blue color component
# - transparency: The transparency value of the colors channel

class gene():
    def __init__(self):
        self.coord_1 = random.randint(0, image_width), random.randint(0, image_height)
        self.coord_2 = random.randint(0, image_width), random.randint(0, image_height)
        self.coord_3 = random.randint(0, image_width), random.randint(0, image_height)
        self.colorR = random.randint(0, 255)
        self.colorG = random.randint(0, 255)
        self.colorB = random.randint(0, 255)
        self.transparency = 30