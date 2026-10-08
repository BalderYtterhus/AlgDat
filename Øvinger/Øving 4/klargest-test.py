#!/usr/bin/python3
# coding=utf-8
import random

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nedre, og muligheten for å generere
# tilfeldige instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å justere på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres.
random_tests = 10
# Laveste mulige antall tall i generert instans.
numbers_lower = 3
# Høyest mulig antall tall i generert instans.
numbers_upper = 8
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0

def k_largest(A, n, k):
    if k == 0 or n == 0:
        return []
    
    m = get_pivot(A) # Riktig pivot

    smaller = [num for num in A if num < m]
    equal = [num for num in A if num == m]
    bigger = [num for num in A if num > m]

    if len(bigger) == k: 
        return bigger
    
    if len(bigger) < k:
        diff = k - len(bigger)# antall tall man må legge til
        # Ta diff tall fra equal
        for i in range(len(equal)):
            bigger.append(equal[i])
            diff -= 1

            if diff == 0: 
                return bigger
        
        # Ta diff tall fra smaller sine største
        remaining_largest = k_largest(smaller, len(smaller), diff)
        bigger.extend(remaining_largest)

        return bigger


    if len(bigger) > k:
        return k_largest(bigger, len(bigger), k)


def groups_of_five(l:list):
    return [l[i:i+5] for i in range(0, len(l), 5)] 

def insertion_sort(A):

    for i in range(1, len(A)):
        key = A[i]

        j = i - 1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

    return A

def find_median(A):
    return insertion_sort(A)[len(A)//2]

def get_pivot(l:list):
    medians = []

    for group in groups_of_five(l):
        medians.append(find_median(group)) 


    if len(medians) <= 5:
        return insertion_sort(medians)[len(medians)//2]
    
    return get_pivot(medians)

# Sett med hardkodete tester på format: (A, k)
tests = [
    ([], 0),
    ([1], 0),
    ([1], 1),
    ([1, 2], 1),
    ([-1, -2], 1),
    ([-1, -2, 3], 2),
    ([1, 2, 3], 2),
    ([3, 2, 1], 2),
    ([3, 3, 3, 3], 2),
    ([4, 1, 3, 2, 3], 2),
    ([4, 5, 1, 3, 2, 3], 4),
    ([9, 3, 6, 1, 7, 3, 4, 5], 4),
]

def gen_examples(k, lower, upper):
    for _ in range(k):
        A = [
                random.randint(-50, 50)
                for _ in range(random.randint(lower, upper))
            ]
        yield A, random.randint(0, len(A))


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        numbers_lower,
        numbers_upper,
    ))

failed = False
for A, k in tests:
    answer = sorted(A, reverse=True)[:k][::-1]
    student = k_largest(A[:], len(A), k)

    if type(student) != list:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans:
A: {A}
n: {len(A)}
k: {k}

Metoden må returnere en liste
Ditt svar: {student}
""")
    else:
        student.sort()
        if student != answer:
            if failed:
                print("-"*50)
            failed = True
            print(f"""
Koden feilet for følgende instans:
A: {A}
n: {len(A)}
k: {k}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")