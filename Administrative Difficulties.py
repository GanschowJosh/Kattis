import math
class car:
    def __init__(self, name, price, pickupCost, driveCost) -> None:
        self.name = name
        self.price = price
        self.pickupCost = pickupCost
        self.driveCost = driveCost
        self.picked = False
        self.currDriver = ""
        
class agent:
    def __init__(self, name) -> None:
        self.name = name
        self.currentCar = ""
        self.outcome = 0

def findCarObj(name): #returns position of car in list as integer
    it = 0
    for item in cars:
        if item.name == name:
            return it
        it+=1

def findAgentObj(name): #returns position of car in list as integer
    it = 0
    for item in agents:
        #print(f"{name} {item.name} {it}")
        if item.name == name:
            return it
        it+=1
        if it > len(agents):
            return -1

cases = int(input())
n, m = list(map(int, input().split()))
cars = []
agents = []
for _ in range(n):
    carname, carprice, carpickupcost, cardrivecost = input().split()
    cars.append(car(carname, int(carprice), int(carpickupcost), int(cardrivecost)))

for _ in range(m):
    t, s, e, x = input().split()
    if findAgentObj(s) == -1 or findAgentObj(s) == None:
        agents.append(agent(s))
    if e == "p":
        it2 = findCarObj(x)
        cars[it2].picked = True
        it = findAgentObj(s)
        if agents[it].currentCar != "":
            agents[it].outcome = -1
        else:
            agents[it].currentCar = x
            agents[it].outcome += cars[it2].pickupCost
    elif e == "r":
        it = findAgentObj(s) #finding current pertinent agent\
        #print(f"agent number {it}")
        it2 = findCarObj(agents[it].currentCar) #finding agents current car
        if cars[it2].picked != True: #car wasnt in use, can't be returned
            agents[it].outcome = -1
        else: #car was in use, can be returned
            if agents[it].outcome != -1: #dont bother with calculation if already an inconsistent outcome
                agents[it].outcome += (cars[it2].driveCost * int(x)) #calculating outcome with the drive cost of the car and miles driven
            agents[it].currentCar = ""
            cars[it2].picked = False 
    elif e == "a":
        it = findAgentObj(s)
        it2 = findCarObj(agents[it].currentCar)
        #print(f"agent {it} car {it2}")
        if it2 is None: #car wasn't in use, cant have an accident
            agents[it].outcome = -1
        else:
            if agents[it].outcome != -1:
                agents[it].outcome += math.ceil(cars[it2].price * (int(x)/100))


        
for agent in sorted(agents, key=lambda x: x.name):
    if agent.currentCar != "":
        agent.outcome = -1
    print(f"{agent.name} {agent.outcome if agent.outcome >-1 else 'INCONSISTENT'}")

