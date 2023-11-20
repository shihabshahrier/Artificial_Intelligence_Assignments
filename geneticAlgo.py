import random as rand

class GeneticAlgo:
    def __init__(self, transactions, init_population_size):
        self.transactions = transactions
        self.trans_lenght = len(transactions)
        self.init_population_size = init_population_size

    def generatePopulation(self):
        populations = []
        for _ in range(self.init_population_size):
            population = [rand.randint(0, 1) for _ in range(self.trans_lenght)]
            populations.append(population)  
        return populations

    def checkFitness(self, population):
        fitness_values = []
        for indiv in population:
            trans_sum = 0
            for i in range(self.trans_lenght):
                if indiv[i] == 1:
                    trans_type, trans_amount = self.transactions[i]
                    if trans_type == "l":
                        trans_sum -= int(trans_amount)
                    else:
                        trans_sum += int(trans_amount)
            fitness_values.append(trans_sum)
        return fitness_values

    def selectParents(self, population, fitness):
        wgt = []
        for fit in fitness:
            wgt.append(fit / sum(fitness))
        parentX, parentY = rand.choices(range(len(population)), weights=wgt, k=2)
        return population[parentX], population[parentY]

    def crossOver(self, xx, xy):
        cross_section = rand.randint(0, self.trans_lenght - 1)
        child = xx[cross_section:] + xy[:cross_section]
        return child

    def mutate(self, child):
        gene = rand.randint(0, len(child) - 1)
        child[gene] = 1 - child[gene]
        return child

    def produce(self, limit, mutation_rate):
        init_population = self.generatePopulation()
        for _ in range(limit):
            fitness = self.checkFitness(init_population)
            __population = []
            for _ in range(len(init_population)):
                xx, xy = self.selectParents(init_population, fitness)
                child = self.crossOver(xx, xy)
                if rand.random() < mutation_rate:
                    child = self.mutate(child)
                if all(c == 0 for c in child):
                    __population.append(child)
                    continue
                if self.checkFitness([child])[0] == 0:
                    result = "".join(map(str, child))
                    return result
                __population.append(child)
            init_population = __population
        return -1

def readFile():
    transactions = []
    with open("input.txt") as file:
        n = int(file.readline())
        for i in range(n):
            line = file.readline().split()
            transactions.append(line)
    return transactions

if __name__ == "__main__":
    transactions = readFile()    
    init_population = 10
    limit = 10**4
    mutation_rate = 0.05
    genetic_algo = GeneticAlgo(transactions,init_population)
    result = genetic_algo.produce(limit, mutation_rate)
    print(result)
