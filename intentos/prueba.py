import random

seed = 123456
random.seed(seed)

N = 40
k = 10
valores = [random.randrange(200) for _ in range(N)]
pesos = [random.randrange(10) for _ in range(N)]
max_peso = 150
MAX_ITER = 1000

def fitness(x):
    f = 0
    p = 0
    for i in range(N):
        f += x[i] * valores[i]
        p += x[i] * pesos[i]
        if p > max_peso:
            f = 0
            break
    return f

def peso(x):
    p = 0
    for i in range(N):
        p += x[i] * pesos[i]
    return p

def añadir_k(l, k):
    while len(l) < k:
        sol = [random.choice([0, 1]) for _ in range(N)]
        if sol in l:
            continue
        l.append(sol)
    return l

def inicial():
    return añadir_k([], k)

"""
def suma_fitness(l):
    return sum([fitness(x) for x in l])

def prob(x, l, total):
    if x not in l:
        return 0
    return fitness(x) / total
"""

def prob(x):
    return fitness(x)

def sample(l):
    l = añadir_k(l, 4 * k)
    muestra = []
    while len(muestra) < k:
        x = random.choice(l)
        if x in muestra:
            continue
        y = random.randint(0, 199 * N)
        if prob(x) >= y:
            muestra.append(x)
    return muestra

def algoritmo():
    gen = inicial()
    for i in range(MAX_ITER):
        gen = sample(gen)
    maxi = gen[0]
    max_fit = fitness(maxi)
    for x in gen:
        if fitness(x) > max_fit:
            maxi = x
            max_fit = fitness(x)
    return maxi, max_fit


print("Valores: ", valores)
print("Pesos:", pesos)
m, f = algoritmo()
print("Se alcanaza el máximo en", m, "con fitness", f, "y peso", peso(m))
print("\n\n\n\n")