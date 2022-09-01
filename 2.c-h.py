student = {
    "first_name" : "Kavya",
    "last_name" : "Addalapudi",
    "gender" : "Female",
    "age" : 22,
    "marital_status" : "single",
    "skills" : "Java, Python",
    "country" : "India",
    "city" : "Vijayawada",
    "address" : "Penamaluru-521139"
}
#Get the length of the student dictionary
#use the length function to get the length of dictionary
print("Length of dictionary is : %d" %len(student))

#Get the value of skills and check the data type, it should be a list

print(student["age"], type("age"))

#Modify the skills values by adding one or two skills

#To the key skiils we have added one more skill to the list
student["skills"] = "Java, Python, Web development"
print(student)

#Converting the keys of student dictionary to a list
keysList = list(student.keys())
print(keysList)

#Converting the values of student dictionary to a list
valuesList = list(student.values())
print(valuesList)
