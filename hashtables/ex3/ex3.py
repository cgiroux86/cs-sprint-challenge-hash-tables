def intersection(arrays):
    cache = dict()
    total = len(arrays)
    results = []
    for arr in arrays:
        for a in arr:
            if a not in cache:
                cache[a] = 1
            else:
                cache[a] += 1
    for key, val in cache.items():
        if val == total:
            results.append(key)
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
