#Part A
#comment 1: 
x = 10
print(x > 5)
print(x == 10)
print(x < 3)

#Part B
#comment 2: 
a = 8
b = 12
print(a < 10 and b > 10)
print(a > 10 or b > 10)

#comment 3:
age = 19
if age >=18:
    print('Adult')

#comment 4:
marks = 45
if marks >=50:
    print('Pass')
else:
    print('Fail')

#Part B
#comment 1: Ask the uner for a number. If the number is positive, print "Positive number".
Num = int(input("Enter your Num: "))
if (Num>0):
     print("Positive number")

#comment 2: Ask the user for temperature, IF temperature is above 30, print "IT is a hot day".
Tem = int(input("Enter today's Temperature: "))
if (Tem>=30):
     print("It is a Hot")

#comment 3: Ask the user for a password length. If the length is less than 8, print "Password too short".
Pass = int(input("Enter your Password: "))
length = len(Pass)
if (length < 8):
     print("Password too short")
else:
     print("Good Passwprd length")

#comment 4: Ask the user for exam markes. If marks are 100, print "Perfect score!".
Mark = int(input("Enter exam marks: "))
if (Mark<=100):
     print("Perfect score")

#comment 5: Ask the user for a shopping amount. If amount is greather than or equal to 200, print "You qualify for a bonus voucher"
Amount = int(input("Enter the shopping amount: "))
if (Amount>=200):
     print("You qualify for a bonus voucher")

# Part C
#comment 6: Ask the user for a number and check whether it is even or odd.
number=int(input("Enter a number: "))
if(number%2 ==0):
    print("The number is even")
else:
    print("The numver is Or")

#comment 7: Ask the user for age and print "Adult" or "Minor".
age=20
if(age>18):
    print("You are Minor")
else:
    print("You are Adult")

# #comment 8: Ask the user for a username. If it matches admin, print"Access granted", otherwise print "Access denied".
admin_user =  "nicolewallace"
username = input("Enter your username:")
if username == admin_user:
    print("Access granted")
else:
    print("Access denied")

#9 Ask the user for a product price. If the price is 50 or more, print "Free shipping", otherwise print "Shipping charges apply".
price= float(input("Enter a product price:"))
if price >=50:
    print("Free shipping")
else:
    print("Shipping charges apply")

#10 Ask the user for attendance percentage. If it is 80 or above, print "Allowed to sit the quiz", otherwise print "Attendance too low".
attendance = int(input("Enter the attendance percentage"))
if attendance >= 80:
    print("Allowed to sit the quiz")
else:
    print("Attendance too low")
#Part D -Coding Practice: if-elif-else

#11 Create a grade calculator: 90-100 = A, 75-89 = B, 60-74 = C, below 60 = D.
grade = int(input("Enter your grade:"))

if grade >= 90:
    print("A")
elif grade >= 75:
    print("B")
elif grade >= 60:
    print("C")
else :
    print("D")

#12 Ask the user for a number. Print "Positive", "Negative", or "Zero".
number = int(input("Enter a number:"))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#13 Ask the user for the current hour (0-23). Print "Morning", "Afternoon", "Evening", or "Invalid time".
hour = int(input("Enter the current hour:"))
if 0 <= hour < 5:
    print("Night") 
elif 5 <= hour < 12:
    print("Morning")
elif 12 <= hour <16:
    print("Afternoon")
elif 16 <= hour <23:
    print("Evening")
else:
    print("Invalid time")

#14 Ask the user for BMI category score and display "Underweight", "Normal", "Overweight", or "Obese" using your own clear ranges.
bmi = float(input("Enter your BMI:"))
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal")
elif 25.0 <= bmi <=29.9:
    print("Overweight") 
else:
    print("Obese")

#15 Create a ticket price checker: age under 5 = Free, 5-12 = Child ticket, 13-64 = Standard ticket, 65+ = Senior ticket
age = int(input("Enter your age:"))
if age < 5:
    print("Free")
elif 5 <= age <= 12:
    print("Child ticket")
elif 13 <= age <= 64:
    print("Standard ticket")
else:
    print("Senior ticket")

#16 Create a traffic-light helper: user enters color and program prints action such as Stop, Ready, or Go. Use if-elif-else, not match-case, for this task
color = input("Enter a color:")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")

#17 Build a simple loan approval decision: income below 40000 = Not eligible, 40000-69999 = Review needed, 70000+ = Eligible
income = int(input("Enter your income"))
if income < 40000:
    print("Not eligible")
elif 40000 <= income <= 69999:
    print("Review needed")
else:
    print("Eligible")



#Part E - Coding Practice: match-case

#18 Ask the user to enter a day number (1-7) and display the matching weekday name.
day = int(input("Enter a day number(1-7):"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thurday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")

#19 Create a menu program where user selects 1 = Add, 2 = View, 3 = Update, 4 = Exit.
menu = int(input("Select a number(1=add, 2=view, 3=update, 4=exit):"))

match menu:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Update")
    case 4:
        print("Exit")
    case _:
        print("Invaild menu")

#20 Ask the user to enter a letter grade (A, B, C, D) and print a short message for each grade.
grade = input("Enter you grade(A,B,C,D):")

match grade:
    case "A":
        print("Excellent! Keep it up.")
    case "B":
        print("Good job! Solid effort.")
    case "C":
        print("Satisfactory performance.")
    case "D":
        print("Needs improvement. Keep practicing")
    case _:
        print("Invalid grade")

#21 Create a fruit selector: apple, banana, orange, mango. Show one healthy message for each
fruit = input("Enter a fruit(apple, banana, orange, mango):")

match fruit:
    case "apple":
        print("Apples are rich in fiber and great for heart health!")
    case "banana":
        print("Bananas provide a fantastic boost of potassium and energy!")
    case "orange":
        print("Orangrs are packed with Vitamin C to boost your immunity!")
    case "mango":
        print("Mangoes are loaded with Vitamin A a Vitamin C for healthy skin!")
    case _:
        print("Healthy choice, but not in our main list!")

#22 Create a transport fare helper: bus, train, ferry. Print a suitable message for each choice and use a default case for invalid input.
transport = input("Enter a transport(bus, train, ferry):")

match transport:
    case "bus":
        print("Buses are a convenient and affordable way to travel locally.")
    case "train":
        print("Trains offer a fast, smooth ride for longer commutes.")
    case "ferry":
        print("Ferries provide a scenic trip across the water.")
    case _:
        print("Invalid choice. Please choose bus, train, or ferry.")




#Part F- Mini Lab Programs (Longer Practice)

#1. Grade Calculator
marks = float(input("Enter the marks:"))
if marks >=90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}.")
if grade in ["A","B"]:
    print("Excellent work.")

#2. Loan Approval Logic System
income = float(input("Enter your monthly income:"))
employment_status = input("Enter your employment status(employed/unemployment):")

if employment_status == "employed" and income >= 3000:
    print("Loan Approved")
elif employment_status == "employed" and income >= 1500:
    print("Loan Under Review")
else:
    print("Loan Rejected")

#3. Restaurant Menu Selector
print("Menu Options:")
print("1. Burger")
print("2. Pizza")
print("3. Pasta")
print("4. Salad")
choice = int(input("Select a menu item number(1-4):"))

match choice:
    case 1:
        print("Selected: Burger | Price: $8.65")
    case 2:
        print("Selected: Pizza | Price: $13.89")
    case 3:
        print("Selected: Pasta | Price: $10.43")
    case 4:
        print("Selected: Salad | Price: $7.38")
    case _:
        print("Invalid choice")

#4. Logic and Access Check
username = input("Enter your username:")
password = input("Enter your password:")
if username == "zaniswet" and password == "devzanihaldersweta123":
    print("Welcome!")
else:
    print("Access Denied.")

#5. Electricity Bill Category
units = float(input("Enter electricity units comsumed:"))
if units < 100:
    print("Low. Tip: Keep up the good work saving energy.")
elif 100 <= units <=300:
    print("Medium. Tip: Unplug unused electronics to lower consumption.") 
else:
    print("High. Tip: Consider using energy-efficient appliances to reduce power.")

#6. Simple Calculator Menu
number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))
operations = input("Choose a operations(+,-,*,/):")
match operations:
    case "+":
        print("Result: {number1 + number2}")
    case "-":
        print("Result: {number1 - number2}")
    case "*":
        print("Result: {number1 * number2}")
    case "/":
        print("Result: {number1 / number2}")
    case _:
        print("Invalid operation.")