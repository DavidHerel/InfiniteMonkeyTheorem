from DNA import DNA
import random

class Population:

    """
    Constructor:
    target - target phrase (e.g. unicorn)
    mutationRate - number, specifying probability of mutation of DNA when creating new element from parents
    popMax - number, specifying maximum elements alive
    population = list which holds current population
    matingPool = list which we will use for our "mating pool"
    finished = are we finished with evolving?
    generations = number of generations
    perfectScore = score we want to achieve
    """
    def __init__(self, target, mutationRate, popMax):
        self.target = target
        self.mutationRate = mutationRate
        self.population = []
        #create population
        for i in range(popMax):
            self.population.append(DNA(len(target)))

        self.matingPool = []
        self.finished = False
        self.generations = 0

        self.perfectScore = 1

    #select best elements in population and put them in mating pool
    def naturalSelection(self):
        self.matingPool.clear()

        #Based on fitness, each member will get added to the mating pool a certain number of times
        #a higher fitness = more intries to mating pool = more likely to be picked as a parent
        #a lower fitness = fewer entries to mating pool = less likely to be picked as a parent
        for i in range(len(self.population)):
            #loopCount is percentage of succes * 100
            loopCount = self.population[i].fitness(self.target)
            loopCount = loopCount*100
            for j in range(int(loopCount)):
                self.matingPool.append(self.population[i])

    #generate new population
    def generate(self):
        #refill population with the children from the mating pool
        for i in range(len(self.population)):
            #take random parents from mating pool
            partnerA = random.choice(self.matingPool)
            partnerB = random.choice(self.matingPool)
            #lets have fun
            child = partnerA.crossover(partnerB)
            #add some mutation
            child.mutate(self.mutationRate)
            #replace new one
            self.population[i] = child
        self.generations+=1

    #get the best element from population
    def getBest(self):
        worldRecord = 0
        index = 0
        for i in range(len(self.population)):
            if (worldRecord < self.population[i].fitness(self.target)):
                worldRecord = self.population[i].fitness(self.target)
                index = i
        if(worldRecord == self.perfectScore):
            self.finished = True

        return self.population[index]

    #Compute average fitness for the population
    def getAverageFitness(self):
        total = 0
        for i in range(len(self.population)):
            total += self.population[i].fitness(self.target)
        return total/len(self.population)

    def allPhrases(self):
        everything = ""
        for i in range(len(self.population)):
            everything += self.population[i].genes + "\n"
        return everything