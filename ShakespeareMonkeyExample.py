#David Herel

#Genetic Algorithm, Evolving Shakespeare

#Using a genetic algorithm to perform a search

# setup()
# # Step 1: The Population
# # Create a population with random DNA

# draw()
# # Step 1: Selection
# # Create an empty mating pool
# #  For every member of the population, evaluate its fitness based on some criteria (objective function)
# # and add it to the mating pool. The more fit it is the more times it appears in mating pool,
# # in order to be more likely to picked for reproduction

# # Step 2: Reproduction
# # Fill the new population by executing the following steps:
# # 1. Pick tow parents objects from the mating pool
# # 2. Crossover -- create a child object by mating these two parents
# # 3. Mutation -- mmutate the childs DNA based on given probability
# # 4. Add the child object to the new population
# # Replace the old population with the new population

# # Rinse and repeat
from Population import Population
import time

def setup():
    target = "To be or not to be"
    popMax=1000
    mutationRate = 0.01

    #create a new population with a target phrase, mutation rate and population max
    population = Population(target, mutationRate, popMax)
    return population

def draw(population):
    #generate mating pool
    population.naturalSelection()
    #create next generation
    population.generate()

    #get best
    population.getBest();

    printAllStats(population)

    #if we found target phrase, stop
    return not population.finished


def main(pop):
    retval = True
    while (retval):
        #create new gens until it gets right element
        retval = draw(pop)
    printAllStats(pop)
    return True

def printAllStats(pop):
    print("Best phrase: " + "{}{}".format("", pop.getBest().genes) + "\n")
    print("Total generations: " + "{}{}".format("", pop.generations) + "\n")
    print("Average fitness: " + "{}{}".format("", pop.getAverageFitness()) + "\n")
    print("-----------------------------------------")

#get statistics for n population
def statistics(pop, n):
    #starting time
    start_time = time.time()
    #iterations
    i = 0
    #sum of all generations
    generationsSum = 0
    #sum of time
    timeSum = 0
    #loop n times of main function
    while(i!=n):
        #when element was found = raise I
        if(main(pop)==True):
            i+=1
            generationsSum+= pop.generations
            #create new generation
            pop = setup()
    #stats sum
    timeSum = (time.time() - start_time)
    generationsSum = generationsSum/n
    timeSum = timeSum/n
    
    print("Average generations: " + "{}{}".format("", generationsSum) + "\n")
    print("Average time: --- %s seconds ---" % (timeSum))

#setup population
population = setup()
#statistics of n populations
statistics(population, 1)

