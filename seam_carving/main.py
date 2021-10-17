#!/usr/bin/python3
# coding=utf-8


def find_path(weights):
    # Skriv koden din her
    pass


# Tester på formatet (vekter, minste mulige vekt på sti).
tests = [
    ([[1]], 1),
    ([[1, 1]], 1),
    ([[1], [1]], 2),
    ([[2, 1], [2, 1]], 2),
    ([[1, 1], [1, 1]], 2),
    ([[2, 1], [1, 2]], 2),
    ([[3, 2, 1], [1, 3, 2], [2, 1, 3]], 4),
    ([[1, 10, 3, 3], [1, 10, 3, 3], [10, 10, 3, 3]], 9),
    ([[1, 2, 7, 4], [9, 3, 2, 5], [5, 7, 8, 3], [1, 3, 4, 6]], 10),
]


# Verifiserer at en løsning er riktig gitt vektene, stien og den minst
# mulige vekten man kan ha på en sti.
def verify(weights, path, optimal):
    if len(path) != len(weights):
        return False, "Stien er enten for lang eller for kort."

    last = -1
    for index, element in enumerate(path):
        if type(element) != tuple:
            return False, "Stien består ikke av tupler."
        if len(element) != 2:
            return False, "Stien består ikke av tupler på formatet (x,y)."
        if index != element[1]:
            return False, "Stien er ikke vertikal."
        if element[0] < 0 or element[0] >= len(weights[0]):
            return False, "Stien går utenfor bildet."
        if last != -1 and not last - 1 <= element[0] <= last + 1:
            return False, "Stien hopper mer enn en piksel per rad."
        last = element[0]

    weight = sum(weights[y][x] for x, y in path)
    if weight != optimal:
        return (
            False,
            "Stien er ikke optimal. En optimal sti ville hatt"
            + "vekten {:}, mens din hadde vekten {:}".format(optimal, weight),
        )

    return True, ""


failed = False

for test, optimal_weight in tests:
    answer = find_path([row[:] for row in test])
    correct, error_message = verify(test, answer, optimal_weight)
    if not correct:
        failed = True
        print(
            'Feilet med feilmeldingen "{:}" for testen '.format(error_message)
            + "{:}. Ditt svar var {:}.".format(test, answer)
        )

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")
