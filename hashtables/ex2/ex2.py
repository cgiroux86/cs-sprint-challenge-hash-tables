#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = dict()
    route = []
    for t in tickets:
        cache[t.source] = t.destination
    start = cache['NONE']
    while start is not 'NONE':
        route.append(start)
        start = cache[start]
    route.append(start)
    return route
