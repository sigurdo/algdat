import random

def partition(A, p, r):
    x = A[r][0]
    i = p - 1
    for j in range(p, r):
        if A[j][0] <= x:
            i = i + 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i + 1] 
    A[i + 1] = A[r]
    A[r] = tmp
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

# liste = [(random.randint(0, 20), random.randint(0, 20)) for i in range(20)]
liste = [(19, 6), (3, 2), (8, 4), (1, 19), (8, 10), (5, 11), (10, 20), (19, 9), (13, 13), (9, 6), (5, 18), (13, 5), (14, 16), (20, 0), (1, 7), (15, 2), (2, 2), (13, 16), (11, 2), (6, 13)]

print(liste)
quicksort(liste, 0, len(liste) - 1)
print(liste)

# Konklusjon: quicksort er faktisk ustabil for partition-rutina er ganske sånn random-aktig fordi når den finner et element som står på feil side av pivot så forskyver den ikke lista, men flytter helt hulter til bulter på de elementene som trengs for at den skal være riktig partisjonert. Den tar altså null hensyn til rekkefølge på ting innad i en partisjon
