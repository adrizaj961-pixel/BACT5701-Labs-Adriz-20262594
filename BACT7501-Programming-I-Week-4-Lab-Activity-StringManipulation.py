#Task 1: Indexing Practice
text= input("Enter a word: ")
print("The first character is:", text[0])
print("The last character is:", text[-1])
print("The third character is:", text[2])

#Task 2: Slicing Practice
text1= input("Enter your name: ")
print("The first three characters are:", text1[0:3])
print("The last two characters are:", text1[-2:0])

#Task 3: Case Conversion
text3= input("Enter a sentence: ")
print("Uppercase:", text3.upper())  
print("Lowercase:", text3.lower())

#ask 4: Replace and Strip
text4= input("Enter a sentence: ")
print(text4.strip())
print(text4.replace(" ", "_"))

#Task 5: Find and Count
text5= input("Enter a sentence: ")
print(text5.find("a"))
print(text5.count("a"))

#Task 6: Split and Join
text6= input("enter comma-separated values (e.g., apple,banana,mango): ")
values = text6.split(",")
print("Split values:", values)
joined = "_".join(values)
print("Joined with underscores:", joined)