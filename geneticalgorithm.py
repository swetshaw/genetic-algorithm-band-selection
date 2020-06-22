# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 11:25:17 2020

@author: Sweta Shaw
"""

import scipy.io
from PIL import Image
import numpy as np

from ga_utility import read_HSI, flatten_data, initiate_population,crossover, mutate, fitness_all
# function for reading the .mat data
# returns 3-d array for hyperspectral image data stored in x and the groud truth info in y


# Driver code starts here
n = 10          # 10 bands required out of 200
ind = 8         # the population is composed of 'ind' no. of individuals
x, y = read_HSI()
X, Y = flatten_data(x,y)

# the population is initialized
population = initiate_population(X, n, ind)
print("population initialized")
#print("Population after initialization : ", population)
generation = 0
while(generation != 3):
    count = 0
    print("Generation : ", generation)
    print("Population in generation {} : {} \n ".format(generation, population))
    offspring_list = []
    # We will select two parents, mate them and store the new offsprings generated in  a different list
    while(count < ind-1):
        print("Iteration {}".format(count))
        p1 = population[count]
        p2 = population[count+1]
        
        #print("population before crossover", population)
        offspring1, offspring2 = crossover(p1, p2, population) #perform a cross-over of p1 and p2
        #print("Population after crossover {} : {}".format(count, population))
        print("offspring 1 : ", offspring1)
        #print("offspring 2 : ", offspring2)
        m_offspring1 = mutate(list(offspring1))
        print("Mutated offspring 1", m_offspring1)
        #m_offspring2 = mutate(offspring2)
        offspring_list.append(m_offspring1)
        #offspring_list.append(m_offspring2)
        count += 1
        
    print("Crossover + mutation done")
    print("creating pool of poulation + offsprings")
    npool = []   
    for items in population:
        #print("item in population {}".format(items))
        npool.append(items)
    for item in offspring_list:
        #print("item in offspring {}".format(item))
        npool.append(item) 
    print("npool : ", npool)
    #npool = population + offspring_list  #merge the initial population with the offsprings
    fitness_list = fitness_all(npool, X, Y) #calculate the fitness score of all the individuals in npool
    print("Fitness of the generation {} calculated {} : ".format(generation, fitness_list))
    scores = []
    for i, item in enumerate(fitness_list):
        scores.append((fitness_list[i], i))
    sorted_score = sorted(scores, reverse=True)   #add descending order
    #print("sorted score", sorted_score)
    sorted_index = []
    for i in range(len(sorted_score)):
        sorted_index.append(sorted_score[i][1])
    #print("Indices of the selected individuals : ", sorted_index)
    next_gen = []
    for index in sorted_index:
        next_gen.append(npool[index])
    print("total population generated after generation {} : {} \n".format(generation, next_gen))
    population = next_gen[0:ind]
    generation += 1

print("The final bands selected are : ", population)  

# fitness of the last generation
print("Final set of {} bands selected are : \n", population[0])
