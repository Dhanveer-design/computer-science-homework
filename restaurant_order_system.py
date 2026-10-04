# Restaurant Order System
# Queue and Stack

queue = []
stack = []

# Menu
menu = {
    1: ("Pizza", 10),
    2: ("Burger", 7),
    3: ("Pasta", 8),
    4: ("Fries", 4),
    5: ("Coke", 2)
}

# Customer 1 arrives
print("Customer 1 has arrived!")

print("Menu:")
for number, item in menu.items():
    print(number, item[0], "-", item[1], "Euro")

order = []

choice = int(input("Customer 1, choose a dish number: "))
order.append(menu[choice])

choice = int(input("Choose another dish number: "))
order.append(menu[choice])

queue.append(("Customer 1", order))

print("Customer 1 has joined the queue.")
print()

# Customer 2 arrives
print("Customer 2 has arrived!")

order = []

choice = int(input("Customer 2, choose a dish number: "))
order.append(menu[choice])

choice = int(input("Choose another dish number: "))
order.append(menu[choice])

queue.append(("Customer 2", order))

print("Customer 2 has joined the queue.")
print()

# Customer 3 arrives
print("Customer 3 has arrived!")

order = []

choice = int(input("Customer 3, choose a dish number: "))
order.append(menu[choice])

choice = int(input("Choose another dish number: "))
order.append(menu[choice])

queue.append(("Customer 3", order))

print("Customer 3 has joined the queue.")
print()

# Serve customers one by one
while queue:

    customer = queue.pop(0)

    name = customer[0]
    order = customer[1]

    print("Now serving:", name)

    total = 0

    print("Bill for", name)

    for item in order:
        print(item[0], "-", item[1], "Euro")
        total = total + item[1]

    print("Total:", total, "Euro")
    print()

    # Put completed bill into stack
    stack.append((name, total))

print("All customers have been served.")

print()
print("Completed bills:")
print(stack)

# Last completed bill
last_bill = stack.pop()

print()
print("Last completed bill:")
print(last_bill)
