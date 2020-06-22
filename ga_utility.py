# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:12:21 2020

@author: Sweta Shaw
"""
import scipy.io
#from PIL import Image
import numpy as np
#import matplotlib.pyplot as plt
#import numpy as np
#import seaborn as sns
#import random
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from statistics import mean

def read_HSI():
    X = scipy.io.loadmat('Indian_pines_corrected.mat')['indian_pines_corrected']
    y = scipy.io.loadmat('Indian_pines_gt.mat')['indian_pines_gt']
    #print(f"X shape: {X.shape}\ny shape: {y.shape}")
    return X, y

# flatten the 3-d data
def flatten_data(x, y):
    X_flat = []
    for i in range(0,200):
        x_flatten = x[:,:,i].flatten()
        X_flat.append(x_flatten)
    y_flat = y.flatten()
    return X_flat, y_flat

# initiate population with 20 individuals out of 200 
# @params: x : hyperspectral 2-d data
#          n : required no. of bands out of 200
#        ind : no. of individuals in the given population
def initiate_population(x, n, ind):
    population = np.zeros((ind, n))
    for i in range(ind):
        for j in range(n):
            population[i][j] = np.random.randint(200)
    return population

def crossover(m1, m2, population):
    mate1 = []
    mate2 = []
    #print("m1", m1)
    #print("m2", m2)
    k = np.random.randint(1,4)
    print("Crossover point : ", k)
    #print("Population inside crossover", population)
    for val in m1:
        mate1.append(val)
    for vals in m2:
        mate2.append(vals)
    #print("mate1", mate1)
    #print("mate2", mate2)
    for i in range(k, len(mate1)):
        mate1[i], mate2[i] = m2[i], m1[i]
    #print("Crossover function returns",mate1)
    #print("Population inside crossover before return statement ", population)
    return mate1, mate2

def mutate(ofsp):
    m_ofsp = []
    m_ofsp.append(ofsp)
    #print("offspring before mutation", m_ofsp)
    k = np.random.randint(len(ofsp))
    #print("size of m_ofsp", m_ofsp[0])
    m_ofsp[0][k] = np.random.randint(200)
    #print("Offspring after mutation", m_ofsp)
    return m_ofsp[0]

# fitness function calculates the fitness of each individual and returns the average score
# @params : x : individual (chromosome)
#           X : Band dataset
#           y : ground truth
def fitness(x, X, y):
    score_list = []
    for i in range(len(x)):
        index = int(x[i])
        x_data = np.reshape(X[index], (21025,1))
        y_data = np.reshape(y, (21025, 1))
        X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.20, random_state=42)
        clf = svm.SVC(decision_function_shape='ovo', probability=True)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        fitness_score = f1_score(y_test, y_pred, average='weighted')
        score_list.append(fitness_score)
        score = mean(score_list)
    print("Score list : ", score_list)
    print("Average Score : ", score)
    return score

def fitness_all(npool, X, Y):
    fitnessScore_list = []
    for i in range(len(npool)):
        x = npool[i]
        score = fitness(x, X, Y)
        fitnessScore_list.append(score)
    return fitnessScore_list
