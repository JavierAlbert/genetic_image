# Image Reconstruction using triangular shapes

Implementation of a genetic algorithm in Python for the purpose of image reconstruction using 100 triangular polygons.

The solution is based on a genetic algorithm where on each generation we select the individuals (group of triangles) that better reconstruct the target image. The hyper parameters of the solution are the number of triangles, the generations, the population size and the mutation rate. Also, we define the base color (background color) to help our solution reach a better reconstruction.

The code is implemented using 3 main classes: Gene, Individual, Population.  

1) The __Gene__ class defines a triangle.    
2) The __Individual__ class contains an group of genes and is able to build an image and calculate the fitness. It is also capable of doing crossover and mutation.  
3) The __Population__ class contains a group of individuals and is capable of performing selection of the fittest individuals and generation evolution.  

Using a typical colored small JPEG image (250*250 pixels) and with default hyper parameters (100 genes, 30 individuals, 4000 generations) the code runs in less than 5 minutes.

## The genetic algorithm

The genetic algorithm chosen is of the typical form:

1) Initial random population    
2) Fitness evaluation  
3) Selection of best individuals inside population  
4) Crossover between selected individuals  
5) Random gene mutation  
6) Back to step 2 until convergence or until end of generations  

Our choices for the imporant steps:

- __Fitness:__ Chose the pixelwise MSE   
- __Selection:__ Each generation selects the best 4 individuals based on fitness (pool)    
- __Crossover:__ For each chile we randomly choose 2 parents from the pool and do crossover with 3 random slice indexes  
- __Mutation:__ A mutation is equal to a random gene  


## Results example

![image](https://user-images.githubusercontent.com/31891596/51468664-37be2500-1d78-11e9-9446-50638b0401ae.jpg)
![ddd](https://user-images.githubusercontent.com/31891596/51468702-460c4100-1d78-11e9-8d37-d6b7f96b749d.JPG)
