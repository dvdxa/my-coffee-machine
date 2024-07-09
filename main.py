from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    match choice:
        case "report":
            coffe_maker.report()
            money_machine.report()
        case "espresso" | "latte" | "cappuccino":
            drink = menu.find_drink(choice)
            if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
            else:
                continue
        case "off":
            break
        case _:
            print(f"Sorry {choice} is not a valid option")
