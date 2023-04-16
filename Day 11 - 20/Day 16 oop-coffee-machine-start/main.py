from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
menu_item = MenuItem()

while True:
    options = menu.get_items()
    choice = input(f"what would like to have{options}: ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        print("good bye 👋")
        break
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
