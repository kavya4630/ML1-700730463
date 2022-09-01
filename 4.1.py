it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#the length of the set it_companies
print("The length of set is : " +str(len(it_companies)))

#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
listCompanies = ["Infosys", "Wipro", "Netflix"]
it_companies.update(listCompanies)
print(it_companies)

#Remove one of the companies from the set it_companies

it_companies.remove("Wipro")
print(it_companies)




#What is the difference between remove and discard
#the remove() method will raise an error if the specified item does not exist, 
#and the discard() method will not.
it_companies.discard("Wipro")
print(it_companies)
#it_companies.remove("Wipro")
