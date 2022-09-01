

#creating a tuple called sisters
sisters = ("Mouni", "Lavanya", "Divya", "Kavi")
#creating a tupke called brothers
brothers = ("Lachi", "Sashi", "Shiva", "Mani", "Pandu")

#joining the two tuples
#using concatination we can add two tuples
siblings = sisters + brothers

print(siblings)
#To find the no. of sibilings we can use length
print("How many siblings do you have ? " + str(len(siblings)))

#First convert the tuple to list.
#Since tuples are immutable it can't be modified, so we convert tuple into list
s = list(siblings)
#Adding father and mother to the newlist
s.append("Ramesh")
s.append("Anjali")
#Now converting the list s to tuple and assigning it to new tuple family_members
family_members = tuple(s)
print(family_members)
