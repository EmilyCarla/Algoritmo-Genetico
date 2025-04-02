import random

POP_SIZE = 10000  # tamanho da população
MUTATION_RATE = 0.1  # taxa de mutação
GENERATIONS = 1000  # máximo de gerações
TARGET_GENES = "AaBbCcDd"  # combinação genética alvo 
GENES = "AaBbCcDd"  # possíveis alelos

# Função de aptidão(fitness) para contar quantos genes estão corretos
def fitness_function(individual):
    return sum(1 for i, j in zip(individual, TARGET_GENES) if i == j)

# inicialização da população com genes aleatórios
def initialize_population(size, length):
    return [''.join(random.choices(GENES, k=length)) for _ in range(size)]

# seleção por torneio
def tournament_selection(population, fitness_values, k=3):
    selected = random.sample(list(zip(population, fitness_values)), k)
    return max(selected, key=lambda x: x[1])[0]

# crossover para combinar dois indivíduos em um ponto aleatório
def crossover(parent1, parent2):
    point = random.randint(1, len(TARGET_GENES) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# mutação para alterar um gene aleatório
def mutate(individual):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, len(individual) - 1)
        new_gene = random.choice(GENES)
        individual = individual[:index] + new_gene + individual[index+1:]
    return individual

# algoritmo genético principal
def genetic_algorithm():
    population = initialize_population(POP_SIZE, len(TARGET_GENES))
    
    for generation in range(GENERATIONS):
        fitness_values = [fitness_function(ind) for ind in population]
        best_individual = max(population, key=fitness_function)
        
        print(f'Geração {generation + 1}: Melhor = {best_individual}, Aptidão = {fitness_function(best_individual)}')
        
        if best_individual == TARGET_GENES:
            print("Combinação genética alvo encontrada!")
            break
        
        new_population = []
        while len(new_population) < POP_SIZE:
            parent1 = tournament_selection(population, fitness_values)
            parent2 = tournament_selection(population, fitness_values)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population[:POP_SIZE]
    
    return best_individual

# execução do algoritmo
best_solution = genetic_algorithm()
print(f'Melhor combinação genética encontrada: {best_solution}')
