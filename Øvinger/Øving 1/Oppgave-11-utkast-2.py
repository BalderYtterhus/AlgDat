import time

# Lager listen
n = 20_000
M = list(range(1, n)) + [0]

# Starter tiden
start_time = time.perf_counter()

def max_permutations(M):
    # Skriv koden din her
    s = set() # Det koden returnerer
    visited = set()


    for start in range(len(M)):
        path = []
        current = start
        start_index = None

        while (current not in path) and (current not in visited): 
            path.append(current)
            visited.add(current)
            current = M[current]

        if current in path:
            for i in range (len(path)):
                if path[i] == current:
                    start_index = i
                    break

            cycle = path[start_index:]

            if len(cycle)>1:
                for element in cycle:
                    s.add(element)

    return s


# Kjøring av kode
result = max_permutations(M)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Runtime: {execution_time}")
    

