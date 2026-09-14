#arimtatic oparator

#task-1

number1=float(input("Enter first number: "))
number2=float(input("Enter second number: "))

print("Addition:",number1+number2)
print("Subtraction:",number1-number2)
print("Multiplication:",number1*number2)
print("Division:",number1/number2)



#task-2

number1=float(input("Enter first number: "))
print("Division:",number1/2)
print("floor Division:",number1//3)

#comparison operator

#task-3

number1=float(input("Enter first number: "))
number2=float(input("Enter second number: "))
print(number1==number2)
print(number1!=number2)
print(number1>number2)
print(number1<number2)
print(number1>=number2)
print(number1<=number2)

#lofical operator

#task-4

Age=int(input("Enter your age: "))
if Age<12 or Age>60:
    print("You are eligible for the movie ticket discount.")
else:
    print("You are not eligible for the movie ticket discount.")

#Assignment operator

#task-5
salary=3000
increase=500
salary+=increase
print("New salary after increase:",salary)
multiplication_factor=2
salary*=multiplication_factor
print("Final salary after multiplication:",salary)

#Membership operator
#task-6

Username={'jhon','maria','alex','sam'}
username=input("Enter your username: ")
if username in Username:
    print("Exists in the list.")
else:
    print("Does not exist in the list.")

#Identity operator
#task-7
x=10
y=10
print(x is y)
print(x == y)
#comment 
Identify operator checks if two variables point to the same object in memory, while the equality operator checks if the values of the variables are equal. 

#Mini Challange
#task-8

Student_mark=float(input("Enter your mark: "))
if Student_mark >= 50:
    print("passed the exam.")
else:
    print("failed the exam.")

#Reflection questions
#Comments
Difference between = and == is that = is an assignment operator used to assign a value to a variable, while == is a comparison operator used to check if two values are equal.
#Comments
To find remainder we can use the modulus operator %.
#comments
And operator explanins that both conditions must be true for the overall conditions.
#comments
In python, the floor division operator // returns the largest interger less than or equal to the result of the division.