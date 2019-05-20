def linear_search(data, value):
    for i, v in enumerate(data):
        if v > value:
            return None
        if v == value:
            return i
    return None


def binary_search(data, value):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = data[mid]
        if guess == value:
            return mid
        elif guess < value:
            low = mid + 1
        else:
            high = mid - 1
