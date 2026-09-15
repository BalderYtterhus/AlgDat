import time

n = 200
mm = list(range(1, n)) + [0]

start_time = time.perf_counter()


def max_permutations(M):
    # Skriv koden din her
    s = set() # Det koden returnerer
    sykel_start = None  

    for start in range(len(M)):
        path = []
        current = start
        start_index = None

        while current not in path: 
            path.append(current)
            current = M[current]

        for i in range (len(path)):
            if path[i] == current:
                start_index = i
                break

        cycle = path[start_index:]

        if len(cycle)>1:
            for element in cycle:
                s.add(element)

    return s



result = max_permutations(mm)
end_time = time.perf_counter()
execution_time = end_time - start_time


print(f"Runtime: {execution_time}")
