MENU = [
    {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        }
    },
    {
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        }
    },
    {
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    },
]
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def select_coffe(choice):
    if choice == 1:
        return MENU["espresso"]
    elif choice == 2:
        return MENU["latte"]
    elif choice == 3:
        return MENU["cappuccino"]


coins = {'quarter': 0.25, "dimes": 0.10, "nickles": 0.05, "penny": 0.01}


def process_coin():
    print("Please insert coins")
    total = 0
    for k, v in coins.items():
        user_input = int(input(f"How many {k} "))
        total += v * user_input
    return total


def check_resource(coffee):
    # for (coff, item_cof), (res, item_res) in zip(coffee["ingredients"].items(), resources.items()):
    #     if res[item_res] < coffee["ingredients"].get(item_res, 0):
    # # if key error is there then the default value will be 0, .get(item)
    for item_res in resources:
        if resources[item_res] < coffee.get(item_res, 0):
            print(f"Sorry there is not enough {item_res}.")
            return False
    return True


def make_coffee(coffee):
    for item_res in resources:
        resources[item_res] -= coffee.get(item_res, 0)


while True:
    choice = input("What would you like? \n1 => espresso\n2 => latte\n3 => cappuccino \n::->")
    # choice = 1
    if choice == "report":
        for item in resources:
            print(f"{resources[item]}: {item}")
        print(f"Money: ${profit}")
    elif choice == "off":
        print("system.exit()")
        break
    else:
        choice = int(choice)
        coffee = list(MENU[choice - 1].keys())[0]
        coffee_description = MENU[choice - 1][coffee]
        # coffee_description = select_coffe(choice)
        is_available = check_resource(coffee_description["ingredients"])
        if is_available:
            user_total = process_coin()
            if user_total > coffee_description["cost"]:
                global profit
                profit += coffee_description["cost"]
                balance = round(user_total - coffee_description["cost"], 2)
                print(f"Here is your balance: {balance}")
                print(f"Here is your {coffee} ☕")
                make_coffee(coffee_description["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded.")
