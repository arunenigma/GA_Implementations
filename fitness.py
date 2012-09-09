__author__ = 'arunprasathshankar'
# Genetic Algorithms to match sakti with shiva
import random
import sys

target_string = 'shiva'
target_length =len(target_string)
class String_Matcher(object):
    population = []
    fitness = 0

    def string_fitness(self,individual):
        for i in range(0,target_length):
            self.fitness += abs(ord(individual[i]) - ord(target_string[i]))
        return self.fitness

    def init_strings_population(self,population_size):
        for i in range (0,population_size):
            individual = ''
            for j in range (0, target_length):
                individual += chr(random.randint(97,122))
            self.population.append(individual)
        return self.population

    def random_optimize(self):
        best_fitness = 99999999999
        best_solution = None
        for i in range(len(self.population)):
            print self.population[i]
        # Get the cost
            fitness = String_Matcher.string_fitness(self,self.population[i])

            # Compare it to the best one so far
            if fitness < best_fitness:
                best_fitness = fitness
                best_solution = self.population[i]
        print best_fitness, best_solution


match = String_Matcher()
match.init_strings_population(100000)
match.random_optimize()
