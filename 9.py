#1 Pound = 0.453592 Kilograms or 1 lb = 0.453592 Kg
pounds = []
kgs = []
n = int(input("Enter number of students : "))
for i in range(0, n):
    wel = int(input())
    pounds.append(wel)
    kgl = wel / 2.2046
    x = round(kgl, 2)
    kgs.append(x)
print(pounds)
print("The weight in kgs is :")
print(kgs)