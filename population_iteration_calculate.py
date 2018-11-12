import math

def makePerson():
    a = ["a1","a2","a3"]
    b = ["b1","b2","b3"]
    c = ["c1","c2","c3"]
    person = []
    for i in a:
        for j in b:
            for k in c:
                person.append("_".join([i, j,k]))
    return person
    
    
def makePopulation(popSize):
    population = []
    for p in range(popSize):
        person = makePerson()
        population.append(person)
    return population

optionsPerPerson = 27

popSize = 5

population = makePopulation(popSize)

iterations = []

combinations = 1
for p in range(popSize):
    combinations=combinations*optionsPerPerson
print "possible combinations ", combinations




p1 = makePerson()
p2 = makePerson()
p3 = makePerson()
p4 = makePerson()
p5 = makePerson()

populations = []
repeat = 0
count = 0
for a in p1:
    count+=1
    print count
    for b in p2:
        for c in p3:
            for d in p4:
                for e in p5:
                    x = [a,b,c,d,e]
                    exists = False
                    for p in populations:
                        if set(x)==set(p):
                            exists==True
                            break
                    if exists == False:
                        populations.append(x)                        

print len(populations)