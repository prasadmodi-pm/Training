# Map
a = [1,6,9,10]

Cube = list(map(lambda x: x**3, a))
print Cube

#Filter

n = range(10,15)
x = list(filter(lambda j: j > 0, n))
print x

#Reduce

h = reduce((lambda p,k: p*k), [10,2,6])
print h