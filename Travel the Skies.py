from collections import defaultdict
def isoptimal(k, n, m, flights, customers):
    #create a graph to represent flights
    graph = defaultdict(lambda: defaultdict(list))
    for u, v, d, z in flights:
        graph[d][u].append((v, z))

    #create a dict to store customers at each airport for each day
    airportcustomers = defaultdict(lambda: defaultdict(int))
    for a, b, c in customers:
        airportcustomers[b][a] += c
    
    #simulating flights for each day
    for day in range(1, n+1):
        #for each airport, try to fill flights
        for airport in range(1, k+1):
            #sorting flights by capacity to prioritize filling larger flights
            for dest, capacity in sorted(graph[day][airport], key=lambda x: -x[1]):
                passengers = min(airportcustomers[day][airport], capacity)
                if passengers < capacity:
                    return "suboptimal"

                airportcustomers[day][airport] -= passengers
                airportcustomers[day+1][dest] += passengers
    
        #move remaining customers to next day
        for airport in range(1, k+1):
            airportcustomers[day+1][airport] += airportcustomers[day][airport]
        
    return "optimal"

k, n, m = list(map(int, input().split()))
flights = [tuple(map(int, input().split())) for _ in range(m)]
customers = [tuple(map(int, input().split())) for _ in range(k*n)]

print(isoptimal(k, n, m, flights, customers))