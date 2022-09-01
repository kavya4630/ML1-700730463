A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Join A and B
AUB = A.union(B)
print(AUB)
#Find A intersection B
AIB = A.intersection(B)
print(AIB)
#Is A subset of B
print(A.issubset(B))
#Are A and B disjoint sets
print(A.isdisjoint(B))
#Join A with B and B with A
join_AB = A.update(B)
print(join_AB)
join_BA = B.update(A)
print(join_BA)
#What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#Delete the sets completely
A.clear()
B.clear()
#Convert the ages to a set and compare the length of the list and the set.
ageSet = set(age)
print(len(age) == len(ageSet))