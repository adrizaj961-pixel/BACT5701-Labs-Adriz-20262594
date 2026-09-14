#Part 1
# Task-1:
def welcome():
    print("Welcome to Python Lab")
welcome()

# Task-2:
def name(name):
    print(f"Hello {name}")
name("Adriz")

# Task-3:
def add_numbers(num1,num2):
    return num1+num2
result=add_numbers(10,20)
print(result)

# Task-4:
def check_even_odd(number):
    if number % 2 ==0:
        return "Even"
    else: 
        return "Odd"
result=check_even_odd(56)
print(result)

#Part-2
# Task-5:
number=1
while number <=5:
    print(number)
    number +=1

# Task-6:
total = 0
while True:
    number= int(input("Enter a number(0 to stop):"))
    if number ==0:
        break
    total += number
    print("Total:",total)

#Task-7:
password = ""
while password !="admin123":
    password = input("Enter password:")
    if password !="admin123":
        print("Incorrect password. Try again.")
print("Loged in")

#Task-8
total= 0
while True:
    price = float(input("Enter item price(0 to finish):"))
    if price ==0:
        break 
    total +=price

#Part 3: 
# Task 9: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Task 10: Calculate total from list [100, 200, 300]
prices = [100, 200, 300]
list_total = 0
for price in prices:
    list_total += price
print(f"List Total: {list_total}")

# Task 11: Print items from list
items = ["Laptop", "Mouse", "Keyboard"]
for item in items:
    print(item)

# Task 12: Print items with index
for index, item in enumerate(items):
    print(f"Index {index}: {item}")

#Part 4:
# Task 13:
def sum_input_numbers():
    total = 0
    num = float(input("Enter a number to add (0 to stop): "))
    while num != 0:
        total += num
        num = float(input("Enter a number to add (0 to stop): "))
    return total


# Task 14:
def calculate_list_total(number_list):
    total = 0
    for num in number_list:
        total += num
    return total


# Task 15:
def display_inventory(item_names, item_prices):
    for i in range(len(item_names)):
        print(f"Item: {item_names[i]} | Price: ${item_prices[i]:.2f}")

# Part 5:
#1.
# 1. Create add_items() using while loop
def add_items():
    prices = []
    while True:
        price = float(input("Enter item price (-1 to finish): "))
        if price == -1:
            break
        prices.append(price)
    return prices


# 2. Create calculate_total() using for loop
def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total


# 3. Create display() function
def display(prices, total):
    print("\n--- Summary ---")
    for index, price in enumerate(prices, start=1):
        print(f"Item {index}: ${price:.2f}")
    print(f"Total: ${total:.2f}")

    # Challenge Task logic
    if total > 500:
        print("Status: Approved")
    else:
        print("Status: Not Approved")


# 4. Main program
def main():
    item_prices = add_items()
    total_cost = calculate_total(item_prices)
    display(item_prices, total_cost)


# Execute main program
main()