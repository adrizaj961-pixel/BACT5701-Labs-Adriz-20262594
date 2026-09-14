#Part-1:List Practice:
#1 Create a list of 5 numbers and print all elements.
number =[22,24,26,28,30]
print(number)
#2 print the first and last element of the list
print(number[0])
print(number[4])
#3 Add a new number to the list using append()
number.append(32)
print(number)
#4 Insert a number at position 2.
number.insert(1, 34)
print(number)
#5 Remove one elements from the list.
number.remove(28)
print(number)

#Part-2:Tuple Practice:
#6 Create a tuple with 4 colors and print all values
color=("Pink","Yellow", "Red", "Blue")
print(color)
#7 Print the second element
print(color[1])
#8 Count how many times a value appears in a tuple.
print(color.count("Blue"))
#Part-3:Dictionary Practice:
#9 Create a dictionary with name, age and city.
student ={
    "name":"Adriz",
    "age":"21",
    "city":"Auckland"
}
print(student)
#10 Print each value using keys.
print(student["name"])
print(student["age"])
print(student["city"])
#11 Add a new key to the dictionary
student["course"]= "IT"
print(student)
#12 Update the age value.
student['age']= 25
print(student)
#13 Remove one key from the dictionary.
student.pop("course")
print(student)
# Part-5:Logic Building
#17 Find the sum of numbers in a list.
number=[16,17,18,19,20]
print(number)
total = sum(number)
print(f"The largest number in the list is {total}")
#18 Find the largest number in a list.
largest= max(number)
print(f"The larget number in the list is (largest)")