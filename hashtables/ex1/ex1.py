def get_indices_of_item_weights(weights, length, limit):
    cache = dict()

    for i, w in enumerate(weights):
        difference = limit - w
        if difference in cache:
            return (i, cache[difference])
        else:
            cache[w] = i

    return None

    return None
