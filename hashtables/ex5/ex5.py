# Your code here
import re
from functools import reduce


def finder(files, queries):
    cache = dict()
    result = []

    for f in files:
        split = re.split('/', f)[-1]
        if split in cache:
            cache[split] = [cache[split], f]
        else:
            cache[split] = f

    for q in queries:
        if q in cache:
            result.append(cache[q])
    if result and type(result[0]) is list:
        return list(reduce(lambda a, b: a + b, result))
    else:
        return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
