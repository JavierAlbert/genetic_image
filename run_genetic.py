import population
import numpy as np
from PIL import Image, ImageDraw
from skimage import img_as_float
from IPython.display import display

##########
# This is used to load an image on Google Colab
# Needs to be changed for loading from computer
from google.colab import files
from io import BytesIO

# Image must be called "image.jpg"
uploaded = files.upload()
im = Image.open(BytesIO(uploaded['image.jpg']))
target_image = img_as_float(np.asarray(im))
##########


POPULATION_SIZE = 30
NUM_TRIANGLES = 100
MUTATION_RATE = 0.02
BASE_COLOR = 'white'
GENERATIONS = 4000

if __name__ == "__main__":

    # Get the target image size
    image_height = target_image.shape[0]
    image_width = target_image.shape[1]

    # Initialize
    popu = population()

    # Run for the number of generations
    for i in range(GENERATIONS):
        if i % 500 == 0:
            print("Running generation number: " + str(i))
        popu.evolve()

    # Display target image and best reconstruction
    sorted_ind = sorted(popu.pop, key=lambda x: x.fitness, reverse=True)
    display(im)
    display(sorted_ind[0].image)