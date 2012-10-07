__author__ = 'arunprasathshankar'
# Using Genetic Algorithms to simulate my name ==> 'arun'
import random
import sys

target_string = 'arun'
target_length =len(target_string)

class String_Matcher(object):

    population = []
    def string_fitness(self,individual):
        fitness = 0
        for i in range(0,target_length):
            fitness += abs(ord(individual[i]) - ord(target_string[i]))
        return fitness

    def init_strings_population(self,population_size):
        for i in range (0,population_size):
            individual = ''
            for j in range (0, target_length):
                individual += chr(random.randint(97,122))
            String_Matcher.mutate_string(self,individual)
            self.population.append(individual)
        return self.population

    # random optimization
    # not very effective

    def random_optimize(self):
        best_fitness = 999999
        best_solution = None
        for i in range(len(self.population)):
            print self.population[i]
        # Get the cost
            fitness = String_Matcher.string_fitness(self,self.population[i])

            # Compare it to the best one so far
            if fitness < best_fitness:
                best_fitness = fitness
                best_solution = self.population[i]
        return best_fitness, best_solution

    def mutate_string(self,individual):
        i = random.randint(0,target_length - 1)
        c = chr(random.randint(97,122))
        individual = individual[0:i] + c + individual[i+1:]
        return individual

    def crossover(self,s1,s2):
        i = random.randint(1,target_length-2)
        return s1[0:i] + s2[i:]

    # Optimizing solution using GA

    def genetic_optimize(self,mutation_probability,max_iterations,elite):
        population = self.population
        print('Max iterations ==> %d' % max_iterations)
        original_population_size = len(population)
        top_elite = int(elite * original_population_size)
        print top_elite
        for i in range(max_iterations):
            individual_scores = [(String_Matcher.string_fitness(self,pop),pop) for pop in population]
            individual_scores.sort()
            #print individual_scores
            ranked_individuals = [individual for (score,individual) in individual_scores]
            population = ranked_individuals[0:top_elite]
            #print candidates

            # Add mutated and bred forms of the winners
            while len(population) < original_population_size:
                if random.random() < mutation_probability:
                    # Mutation
                    c = random.randint(0,top_elite)
                    population.append(String_Matcher.mutate_string(self,ranked_individuals[c]))
                else:
                    # cross over
                    c1 = random.randint(0,top_elite)
                    c2 = random.randint(0,top_elite)
                    population.append(String_Matcher.crossover(self,ranked_individuals[c1],ranked_individuals[c2]))
            print('iteration ==> %d \t best fitness ==> %d' % (i,individual_scores[0][0]))
            print('individual ==> %r' % (individual_scores[0][1]))

            if not individual_scores[0][0] != 0:
                return individual_scores[0][1]
            return individual_scores[0][1]

match = String_Matcher()
match.init_strings_population(1000000)
match.random_optimize()
match.genetic_optimize(0.25,1000,.01)


