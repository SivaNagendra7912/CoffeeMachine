menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def avail_resource(item_detail, still_resources):
    itm_rsr = item_detail["ingredients"]
    if still_resources["water"] >= itm_rsr["water"] and still_resources["milk"]:
        if itm_rsr["milk"] and still_resources["coffee"] >= itm_rsr["coffee"]:
            return True
        else:
            return False
    else:
        return False


print("\n!!!!! WELCOME TO COFFEE MANIA !!!!!!\n")
total_money = 0
end_game = False
while not end_game:
    operation_on_machine = input("Buy Product('b'), Monitor Resources and Money('m'), Exit('e'): ").lower()
    if operation_on_machine == 'b':
        item = input('Enter what type of coffee you want: ( espresso / latte / cappuccino ): ')
        item_resources = menu[item]
        for_money = avail_resource(item_resources, resources)
        if for_money:
            print("Insert Money: ")
            money = process_coins()
            remain = round(money - item_resources["cost"], 2)
            if remain == 0:
                money += item_resources["cost"]
                print(f"Here is your {item}, ENJOYYY")
                resources['milk'] -= item_resources['ingredients']['milk']
                resources['water'] -= item_resources['ingredients']['water']
                resources['coffee'] -= item_resources['ingredients']['coffee']
                total_money += item_resources["cost"]
            elif remain < 0:
                end_game = True
                print("Please give Sufficient money for the product")
            else:
                money += item_resources["cost"]
                print(f"Here is your {item}, ENJOYYY")
                print(f"Take your Change: {remain}")
                resources['milk'] -= item_resources['ingredients']['milk']
                resources['water'] -= item_resources['ingredients']['water']
                resources['coffee'] -= item_resources['ingredients']['coffee']
                total_money += item_resources["cost"]
        else:
            print("sorry!!! Insufficient Resources Available")
            end_game=True
    elif operation_on_machine == 'm':
        print(f"Resources Available: \nWater: {resources['water']}\nMilk: { resources['milk'] }")
        print(f"Coffee: {resources['coffee']}\nMoney: {total_money}")
    elif operation_on_machine == 'e':
        print("Thank you!!!, Visit Again")
        end_game = True
    else:
        print("!!!Please enter a valid input to the Machine!!!")
