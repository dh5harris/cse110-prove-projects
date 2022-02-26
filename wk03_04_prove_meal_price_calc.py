# prompts
child_meal_price = float(input("\nWhat is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of a adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

# calculations
child_subtotal = child_meal_price * children
adult_subtotal = adult_meal_price * adults
subtotal = child_subtotal + adult_subtotal
tax = tax_rate / 100
sales_tax = tax * subtotal
total = subtotal + sales_tax

# totals
print(f'\nSubtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}\n')

# tips
tip_rate = subtotal * .2
print(f'The suggested tip at a rate of 20% is ${tip_rate:.2f}')
tip = float(input('How much of a tip would you like to give? '))
balance = tip + total

# final balance and payment
print(f'\nBalance: ${balance:.2f}')
payment = float(input("What is the payment amount? "))
change = payment - (total + tip)
print(f'Change: ${change:.2f}\n')

# thank you
print('Thank you for your business. Please come again.\n')