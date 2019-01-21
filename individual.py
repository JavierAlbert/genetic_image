import gene
import random
import numpy as np
from PIL import Image, ImageDraw
from skimage import img_as_float
from skimage.measure import compare_mse as mse

# The class individual represents a collection of triangles
# It can be used to initialize a new individual or to generate a new individual
# given 2 parent individuals

# It has 3 attributes:
# - genes: A collection of genes (triangles)
# - image: The resulting image when drawing the triangles
# - fitness: The fitness value of the resulting image compared to target

# It has 4 methods:
# - cross: Perform crossover for when initializing from 2 parents
# - mutate: Perform random mutation of some genes
# - build_image: Builds the image using the triangles
# - calculate_fitness: Calculates the fitness against target image

class individual():

    def __init__(self, parent1=None, parent2=None):

        # We build a new individual either by random genes or by crossover
        # and mutation from 2 parents. Then we build the image and calculate
        # the fitness

        self.genes = []
        if (parent1 == None and parent2 == None):
            for i in range(NUM_TRIANGLES):
                self.genes.append(gene())
        else:
            self.cross(parent1, parent2)
            self.mutate()
        self.image = self.build_image()
        self.fitness = self.calculate_fitness()

    def cross(self, parent1, parent2):

        # Cross over is performed by randomly selecting 3 slicing points and
        # then merging the slices from the 2 parents. Who goes first is decided
        # randomly with 50% chance

        if np.random.uniform(0, 1) > 0.5:
            parent1, parent2 = parent2, parent1

        cut_index1 = random.randint(0, NUM_TRIANGLES)
        cut_index2 = random.randint(0, NUM_TRIANGLES)
        cut_index3 = random.randint(0, NUM_TRIANGLES)

        self.genes[:cut_index1] = parent1.genes[:cut_index1]
        self.genes[cut_index1:cut_index2] = parent2.genes[cut_index1:cut_index2]
        self.genes[cut_index2:cut_index3] = parent1.genes[cut_index2:cut_index3]
        self.genes[cut_index3:] = parent2.genes[cut_index3:]

    def mutate(self):

        # A gene can mutate (is changed by a new and random gene) with given probability

        mutate_indices = np.where(np.random.uniform(0, 1, NUM_TRIANGLES) < MUTATION_RATE)
        for index in mutate_indices[0]:
            self.genes[index] = gene()

    def build_image(self):

        # Image is constructed by drawing the triangles. Background color is
        # defined to help the algorithm converge. Otherwise the algorithm may
        # focus on finding the background color and not the details of the image

        image = Image.new('RGB', (image_width, image_height), BASE_COLOR)
        draw = ImageDraw.Draw(image, 'RGBA')
        for gene in self.genes:
            draw.polygon([gene.coord_1, gene.coord_2, gene.coord_3],
                         fill=(gene.colorR, gene.colorG, gene.colorB, gene.transparency))
        return image

    def calculate_fitness(self):

        # Calculate fitness by mean pixel squared error. The minus is used so
        # that images with lower MSE have larger fitness values
        fitness = -mse(img_as_float(self.image), target_image)
        return fitness