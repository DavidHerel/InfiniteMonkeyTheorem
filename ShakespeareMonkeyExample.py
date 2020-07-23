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

def setup():
    target = "Felt delete, might cute later."
    popMax=200
    mutationRate = 0.01

    #create a new population with a target phrase, mutation rate and population max
    population = Population(target, mutationRate, popMax)
    return population

def draw(population):
    #generate mating pool
    population.naturalSelection()
    #create next generation
    population.generate()

    #if we found target phrase, stop
    return not population.finished

def displayInfo(population):
    #display current status of population
    answer = population.getBest()
    #print("All phrases: \n" + population.allPhrases())

    print("Best phrase: " + "{}{}".format("", answer.genes) + "\n")
    print("Total generations: " + "{}{}".format("", population.generations) + "\n")
    print("Average fitness: " + "{}{}".format("", population.getAverageFitness()) + "\n")
    #print("Total population: " + "{}{}".format("", len(population.population))+ "\n")
    #print("Mutation rate: " + "{}{}".format("", population.mutationRate) + "\n")


pop = setup()
while(draw(pop)):
    displayInfo(pop)



