List1=[2,4,-6,-8,9,7]
List2=[i for i in List1 if(i>0)]
print (f"positive list = {List2}")

'''square of N no'''
list1= [1,2,3,4,5,6]
list2= [i**2 for i in list1]
print(list2)

'''List of vowels'''
word=input("Enter a string: ")
listVowel=[i for i in word if i in 'aeiouAEIOU']
print(f"vowels are {listVowel}")

'''Ordinal value'''
w=input("Enter any string: ")
OrdinalVal=[ord(i) for i in w ]
print(OrdinalVal)
