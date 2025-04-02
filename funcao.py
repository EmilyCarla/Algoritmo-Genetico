import random

TAMANHO_POPULACAO = 10000  
TAXA_MUTACAO = 0.50  
GERACOES = 1000  # Maximo de gerações
GENES_ALVO = "AaBbCcDd"  
GENES_POSSIVEIS = "AaBbCcDd"  # Possíveis alelos

# Função de aptidão (fitness) -> para contar quantos genes estão corretos
def funcao_aptidao(individuo):
    return sum(1 for i, j in zip(individuo, GENES_ALVO) if i == j)

# Inicializa a população com genes aleatórios
def inicializar_populacao(tamanho, comprimento):
    return [''.join(random.choices(GENES_POSSIVEIS, k=comprimento)) for _ in range(tamanho)]

# Seleção por torneio -> 
def selecao_torneio(populacao, valores_aptidao, k=3):
    selecionados = random.sample(list(zip(populacao, valores_aptidao)), k)
    return max(selecionados, key=lambda x: x[1])[0]

# Crossover -> para combinar dois indivíduos em um ponto aleatório
def crossover(pai1, pai2):
    ponto = random.randint(1, len(GENES_ALVO) - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

# Mutação -> para alterar um gene aleatório
def mutacao(individuo):
    if random.random() < TAXA_MUTACAO:
        indice = random.randint(0, len(individuo) - 1)
        novo_gene = random.choice(GENES_POSSIVEIS)
        individuo = individuo[:indice] + novo_gene + individuo[indice+1:]
    return individuo

# Algoritmo genético principal
def algoritmo_genetico():
    populacao = inicializar_populacao(TAMANHO_POPULACAO, len(GENES_ALVO))
    
    for geracao in range(GERACOES):
        valores_aptidao = [funcao_aptidao(ind) for ind in populacao]
        melhor_individuo = max(populacao, key=funcao_aptidao)
        
        print(f'Geração {geracao + 1}: Melhor = {melhor_individuo}, Aptidão = {funcao_aptidao(melhor_individuo)}')
        
        if melhor_individuo == GENES_ALVO:
            print("Combinação genética alvo encontrada!")
            break
        
        nova_populacao = []
        while len(nova_populacao) < TAMANHO_POPULACAO:
            pai1 = selecao_torneio(populacao, valores_aptidao)
            pai2 = selecao_torneio(populacao, valores_aptidao)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.extend([mutacao(filho1), mutacao(filho2)])
        
        populacao = nova_populacao[:TAMANHO_POPULACAO]
    
    return melhor_individuo

# Execução 
melhor_solucao = algoritmo_genetico()
print(f'Melhor combinação genética encontrada: {melhor_solucao}')
