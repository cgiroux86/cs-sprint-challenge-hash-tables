def has_negatives(a):
    cache = dict()
    result = []
    for n in a:
        if abs(n) in cache:
            cache[abs(n)] += 1
        else:
            cache[abs(n)] = 1
    for key, val in cache.items():
        if val == 2:
            result.append(key)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
