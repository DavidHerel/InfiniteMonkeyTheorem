import random
import string
import difflib

class DNA:

    """
    Constructor: makes random DNA
    genes = the genetic sequence
    """
    def __init__(self, num):
        self.genes = self.randStr(N=num)


    #Fitness function
    def fitness(self, target):
        countDiff = sum(c1 != c2 for c1, c2 in zip(self.genes, target))
        return len(self.genes) - countDiff

    #Crossover
    def crossover(self, partner):
        #new child
        child = DNA(len(self.genes))

        #fifty fifty swap genoms of parents
        for index in range(len(child.genes)):
            if (bool(random.getrandbits(1))):
                child.genes = child.genes[:index] + self.genes[index] + child.genes[
                                                                                                        index + 1:]
            else:
                child.genes = child.genes[:index] + partner.genes[index] + child.genes[
                                                                                                        index + 1:]

        return child

    #Based on a mutation probabilitz, picks a new random character
    def mutate(self, mutationRate):
        for index in range(len(self.genes)):
            if (random.uniform(0, 1) < mutationRate):
                self.genes= self.genes[:index] + random.choice(string.ascii_letters + string.whitespace + string.digits) + self.genes[index + 1:]


    #create random string of given length
    def randStr(self, chars=string.ascii_letters + string.whitespace + string.digits, N=10):
        return ''.join(random.choice(chars) for _ in range(N))

