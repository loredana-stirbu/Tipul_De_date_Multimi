a=set(input("Dati un sir A: "))
b=set(input("Dati un sir B: "))
print("Caractere ce se intilnesc cel putin o singura data:", a.union(b))
print("Intersectia:", a.intersection(b))
print("Apar in A si nu in B:", a.difference(b))