from data import MENU , resources
import copy
def making_item(amount_left,item):
    for ingredient in MENU[item]['ingredients'].keys():
        amount_left[ingredient] -= MENU[item]['ingredients'][ingredient]
    return amount_left
def check_resource(amount_left,item):
    less_amount_present = 'no'
    for ingredient in MENU[item]['ingredients'].keys():
        if amount_left.get(ingredient,0) < MENU[item]['ingredients'][ingredient]:
            less_amount_present = ingredient
            break
    return less_amount_present
def sufficient_money(price):
    one_coin = int(input("Number of ₹1 coin you are inserting:"))
    two_coin = int(input("Number of ₹2 coin you are inserting:"))
    five_coin = int(input("Number of ₹5 coin you are inserting:"))
    ten_coin = int(input("Number of ₹10 coin you are inserting:"))
    sum_coin = one_coin * 1 + two_coin * 2 + five_coin * 5 + ten_coin * 10
    change = sum_coin - price
    if change < 0:
        return [sum_coin,0]
    else:
        return [change,1]

def run_program():
    is_off = False
    money_got = 0
    amount_left = copy.deepcopy(resources)
    while not is_off:
        costumer_choice = input("What would you like? (espresso/latte/cappuccino):")
        if costumer_choice == "report":
            for item in amount_left:
                unit = "ml" if item != "coffee" else "g"
                print(f"{item.capitalize()}: {amount_left[item]}{unit}")
            print(f"Money : ₹ {money_got}")
        elif costumer_choice == "off":
            is_off = True
        elif costumer_choice not in MENU:
            print("Invalid choice. Please select espresso, latte, or cappuccino.")
        else:
            less_amount = check_resource(amount_left,costumer_choice)
            if less_amount == 'no':
                price = MENU[costumer_choice]["cost"]
                change = sufficient_money(price)
                if change[1] == 0:
                    print(f"Sorry that's not enough money. ₹{change[0]} refunded.")
                else:
                    if change[0] == 0:
                        print(f"Sufficient money inserted! making {costumer_choice}.")
                    else:
                        print(f"making {costumer_choice} change = ₹{change[0]}")
                    money_got += price
                    making_item(amount_left,costumer_choice) #updates amount_left
            else:
                print(f"Sorry there is not enough {less_amount}.")
run_program()
