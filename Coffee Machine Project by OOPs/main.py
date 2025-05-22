from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_off = False

    while not is_off:
        costumer_choice  = input(f"What would you like? {menu.get_items()}: ")
        if costumer_choice == "off":
            is_off = True
        elif costumer_choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(costumer_choice)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)
                    else:
                        print("Insufficient funds. Please try again.")
                else:
                    print("Sorry, not enough resources to make your drink.")
            else:
                print("Sorry, that item is not on the menu. Please try again.")
if __name__ == "__main__":
    main()
# This is the main file that runs the coffee machine program.
