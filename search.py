def linear_search(data, value):
    for i, v in enumerate(data):
        if v > value:
            return None
        if v == value:
            return i
    return None


def binary_search(data, value):
    lo, hi = 0, len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] < value:
            lo = mid + 1
        elif value < data[mid]:
            hi = mid - 1
        else:
            return mid
    return None
