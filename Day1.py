list1 = [3, 4, 2, 1, 3, 3]
list2 = [4, 3, 5, 3, 9, 3]


def find_distance(list1, list2):
    list1.sort()
    list2.sort()

    distance = 0

    for x, y in zip(list1, list2):
        if x > y:
            distance += x - y
        else:
            distance += y - x
    return distance

print(find_distance(list1, list2))