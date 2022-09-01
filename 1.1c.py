ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 19, 26]
#first sort the list elements
ages.sort()
#To find the median we need the mid value of the list
mid = len(ages) // 2
#median is obtained by dividing the middle value by 2
median = (ages[mid] + ages[~mid])/2
print("Median of list is :" + str(median))