import networkx as nx
# import minterpy as mp
import random
#seed = 123456
#random.seed(seed)

#G = nx.read_edgelist("roads.edges", nodetype=int)
#G = nx.read_edgelist("bn-cat-mixed-species_brain_1.edges", nodetype=int)
#G = nx.read_edgelist("olaa.edges", nodetype=int)
G = nx.read_edgelist("ENZYMES_g102.edges", nodetype=int)

MAX_FITNESS = G.order() # Tal y como está definido, el máximo valor que puede tomar el fitness es el número de nodos del grafo
MAX_ITER = 100
SAMPLE_SIZE = 10

def subsets(a):
  l = len(a)
  n = l - 1
  x = [0] * n
  f = [j for j in range(l)]
  r = list()
  
  while n:
    m = [0] + x # insert 0 at the beginning of the bit string forms
    subset = [a[i] for i in range(l) if m[i] == 1] # generate the subset
    
    # and use the subset to generate the subsets for when 1 is inserted at the beginning
    k = [a[0]] + subset
    
    r.append(subset) # add to the table all subsets of bits strigs with prefix 0
    r.append(k) # add to the table all subsets of bits strings with prefix 1
    
    # initialization
    # this is where we choose which j we want to change
    j = f[0]
    f[0] = 0
    
    # if j == n we terminate because we have all the possible bit strings
    if j == n:
      break
     
    # update our array when j != n
    f[j] = f[j + 1]
    f[j + 1] = j + 1
    
    x[j] = 1 - x[j] # complement coordinate j and return to line 8 if j != n
  
  return r

def is_cover(sol, G):
    for u, v in G.edges():
        if sol[u - 1] == 0 and sol[v - 1] == 0:
            return False
    return True

"""
def is_cover(sol, G):
    for u, v in G.edges():
        if sol[u] == 0 and sol[v] == 0:
            return False
    return True
"""

def fitness(sol):
    n = G.order()
    if is_cover(sol, G):
        return n - sum(sol)
    else:
        if sum(sol) >= (2 * n // 3):
            zeros_index = []
            for i in range(len(sol)):
                if sol[i] == 0:
                    zeros_index.append(i)
                    #sol[i] = 1
                    #if is_cover(sol, G):
                    #    print(sol)
                    #    break
                    #sol[i] = 0
            r = subsets(zeros_index)
            r.sort(key=len)
            # r[0] es el conjunto vacío
            for subset in r[1:]:
                for index in subset:
                    sol[index] = 1 # Esto modifica sol porque se pasa por referencia
                if is_cover(sol, G):
                    return n - sum(sol)
                for index in subset:
                    sol[index] = 0
            return 0
        else:
            return 0

def prob(sol):
    return fitness(sol)

def sample(k, skip = []):
    n = G.order()
    sample = []
    while len(sample) < k:
        x = [random.choice([0, 1]) for _ in range(n)]
        if x in sample or x in skip:
            continue
        y = random.randint(0, MAX_FITNESS)
        if fitness(x) > y:
            #print(fitness(x))
            sample.append(x)
    return sample

def init(k):
    n = G.order()
    init = []
    while len(init) < k:
        sol = [random.choice([0, 1]) for _ in range(n)]
        if sol not in init: # Esto se evita usando un set. Aún no tengo claro si necesito índices, o si el set es eficiente en python.
            init.append([random.choice([0, 1]) for _ in range(n)])
    return init

def max_k_fitness(set_sols, k):
    sor = sorted([(fitness(elem), elem) for elem in set_sols])
    return [elem for (_,elem) in sor][-k:]

def max_fitness(set_sols):
    max_value = fitness(set_sols[0])
    max_elem = set_sols[0]
    for elem in set_sols[1:]:
        f = fitness(elem)
        if f > max_value:
            max_value = f
            max_elem = elem
    return max_elem, max_value

def next_gen(curr_gen, k):
    new = sample(k, skip = curr_gen)
    return max_k_fitness(curr_gen + new, k)

def algorithm():
    gen = init(SAMPLE_SIZE)
    for _ in range(MAX_ITER):
        gen = next_gen(gen, SAMPLE_SIZE)
    return max_fitness(gen)

elem, fit = algorithm()
print(f'Máximo valor de fitness ({fit}) encontrado para {elem}, con {sum(elem)} nodos.')

print(is_cover(elem, G))


### A partir de aquí son formas de rellenar


num_ceros = G.order() - sum(elem)
print(num_ceros, "ceros")