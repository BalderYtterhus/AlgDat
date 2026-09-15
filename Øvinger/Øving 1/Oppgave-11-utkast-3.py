import time

# Lager listen
n = 200001
M = list(range(1, n)) + [0]


def max_permutations(M):
    s = set()
    visited = set()

    for start in range(len(M)):
        path = []
        path_index = {}
        current = start

        while (current not in path_index) and (current not in visited):
            path.append(current)
            path_index[current] = len(path) - 1
            visited.add(current)
            current = M[current]

        if current in path_index:
            cycle = path[path_index[current]:]

            if len(cycle) > 1:
                for element in cycle:
                    s.add(element)

    return s


def max_permutations_2(M):
    s = set()
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
            for i in range(len(path)):
                if path[i] == current:
                    start_index = i
                    break

            cycle = path[start_index:]

            if len(cycle) > 1:
                for element in cycle:
                    s.add(element)

    return s


# Måling av algoritme 1
start_time = time.perf_counter()

result_1 = max_permutations(M)

end_time = time.perf_counter()
execution_time_1 = end_time - start_time


# Måling av algoritme 2
start_time = time.perf_counter()

result_2 = max_permutations_2(M)

end_time = time.perf_counter()
execution_time_2 = end_time - start_time


print(f"Algoritme 1: {execution_time_1:.6f} sekunder")
print(f"Algoritme 2: {execution_time_2:.6f} sekunder")
print(f"Algoritme 3 er {execution_time_2/execution_time_1} ganger bedre enn Algoritme 2")
print(f"Samme resultat: {result_1 == result_2}")