
def homeScreen():
    print("Welcome to our resturant, Here's the menu:")
    option = {
        'Pizza': 350,
        'Momo': 200,
        'Burger': 180,
        'Chicken Chowmin': 200,
        'Choila': 150,
        'Katti Roll': 300,
    }

    print('*************************')
    for i, (key, value) in enumerate(option.items(), start=1):
        print(f"{i}. {key} : Rs. {value}")
    print('*************************')

    print("What would you like to order?")
    item_1=input("Enter your order:").strip()

    order_total = 0
    choice = []
    if item_1.isdigit():
        food_index = int(item_1)
        if food_index >=1 and food_index <= len(option):
            food_list = list(option.keys()) # Get all option
            food = food_list[food_index-1]  # Select user option
            choice.append(food)
            print(choice)
            #while True:
            print("Do you want to select more food?")
            #print(f"You selected {food}: Rs. {option[food]}")
            #print("You selected"+{food},"Your total is:", {food.value})
        else:
            print("Invalid Input")
    else:
        if item_1 in option:
            order_total = option[item_1]
            print("Item Added.")
        else:
            print("Invalid Input!")

    another_item = input("Do you want to add more item (y/n)?:").lower()
    if another_item == 'y':
        item_2 = input("Add item to your order list:")
        if item_2 in option:
            print(f"Item {item_2} has been added")
        else:
            print("Option not availiable.")
    elif another_item == 'n':
        exit()
    else:
        print("Enter correct option.")



homeScreen()