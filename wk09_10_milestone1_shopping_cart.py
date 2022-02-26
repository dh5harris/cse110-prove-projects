items = []
prices = []
action = -1

print('\nWelcome to the Shopping Cart Program!')
while action != 5:
    print('\nPlease select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    action = int(input('Please enter an action: '))

# This statement adds items to the shopping cart
# Change the if's to if/elif's

    if action == 1:
        menu_item = input('What item would you like to add? ')
        items.append(menu_item)
        item_price = float(input(f'What is the price of "{menu_item.capitalize()}"? '))
        prices.append(item_price)
        print(f'"{menu_item.capitalize()}" has been added to the cart.')

# This statement displays the contents of the shopping cart
    elif action == 2:
        # Empty cart message
        if len(items) == 0:
            print('The shopping cart is empty.')
        else:
            print('The contents of the shopping cart are: ')
            for i in range(len(items)):
                item = items[i]
                price = prices[i]
                print(f'{(i + 1)}. {item.capitalize()} - ${price:.2f}')
            

# This statement removes an item from the shopping cart
    elif action == 3:
        print('Here is the list of items in the cart:')
        # This if statement shows that the shopping cart is empty and nothing can be removed.
        if len(items) == 0:
            print('Opps! The shopping cart is empty. You need to add an item first.')
        else:
            # this for statement is to show the items in the cart so the user can select what item to remove
            for i in range(len(items)):
                item = items[i]
                price = prices[i]
                print(f'{(i + 1)}. {item.capitalize()} - ${price:.2f}')
            remove = int(input('Which item (number) would you like to remove? '))
            remove_item = remove - 1
            # Added the OR for numbers less than the available indexes.
            if len(items) <= remove_item or remove_item < 0:
                print('Sorry, that is not a valid number.')
            else:
                items.pop(remove_item)
                prices.pop(remove_item)
                print('Itemed removed.')



# This statement gives the price total of the items in the shopping cart
    elif action == 4:
        total = 0
        for price in prices:
            total += price
        print(f'The total price if the items in the shoppong cart is ${total:.2f}')

# This statement quits the program.
print('Thank you. Goodbye.')