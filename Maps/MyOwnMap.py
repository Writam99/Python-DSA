from Map2 import MapNode, Map

m = Map()
for i in range(1,11):
    m[i] = i**2

for i in range(1,11):
    print(m[i], end = ' ')
print()

for i in m.keys():
    print(m[i], end = ' ')