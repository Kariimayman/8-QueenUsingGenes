import numpy as np


def error_calc(vector):
    error = 0
    for Position in range(8):
        r = vector[Position]
        d = Position
        for PositionOther in range(8):
            if PositionOther != Position:
                DD = d - PositionOther
                if DD < 0:
                    DD = DD * -1
                if r == vector[PositionOther]:
                    error = error + 1
                if r + DD == vector[PositionOther]:
                    error = error + 1
                if r - DD == vector[PositionOther]:
                    error = error + 1
    return error


def RankingValues(vector, NumberOfCrosses):
    temp = vector.copy()
    temp.sort()
    lowest = [0 for i in range(NumberOfCrosses)]
    highest = [0 for i in range(int(NumberOfCrosses / 2))]
    for i in range(NumberOfCrosses):
        index = vector.index(temp[i])
        lowest[i] = index
        vector[index] = -1

    temp.reverse()

    for i in range(int(NumberOfCrosses / 2)):
        index = vector.index(temp[i])
        highest[i] = index
        vector[index] = -1

    return lowest, highest


def crossoverAndMutation(low1, low2):
    crossover = low1.copy()
    crossover[7] = low2[7]
    crossover[6] = low2[6]
    crossover[5] = low2[5]
    crossover[4] = low2[4]
    Random = np.random.rand()
    if Random < 0.8:
        i = np.random.randint(8)
        crossover[i] = np.random.randint(8)
    return crossover


while True:
    Population = 16
    NumberOfCrosses = 6
    pop = [[0 for i in range(8)] for j in range(Population)]
    Errors = [-1 for i in range(Population)]
    for PopulationCounter in range(Population):
        for i in range(8):
            pop[PopulationCounter][i] = np.random.randint(8)

    for Iteration in range(1000):
        for PopulationCounter in range(Population):
            Errors[PopulationCounter] = error_calc(pop[PopulationCounter])

        for i in range(len(Errors)):
            if Errors[i] == 0:
                print(pop[i])
                exit()

        low, high = RankingValues(Errors.copy(), NumberOfCrosses)
        Random = np.random.rand()
        if Random < 0.8:
            for changes in range(len(high)):
                pop[high[changes]] = crossoverAndMutation(pop[low[changes * 2]], pop[low[changes * 2 + 1]])

