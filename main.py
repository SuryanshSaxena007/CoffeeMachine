from menu import MENU
from menu import resources
def price(choice):
    new = MENU[choice]["cost"]
    return new



def amount(q,d,n,p):
    payed = round((0.25*q + 0.10*d + 0.05*n + 0.01*p), 2)
    if payed > price(a):
        left = round(payed - price(a), 2)
        return f"Here's ${left} in change.\nHere is your {a}. Enjoy!"

    elif payed == price(a):
        return f"Here is your {a}. Enjoy!"
    else:
        return "Insufficient Amount."

def res():
    n = MENU[a]["ingredients"]
    for key in n:

        if resources[key] < n[key]:
            print(f"Sorry there is not enough {key}")
            return False
        else:
            resources[key] = resources[key] - n[key]
    print("Please insert coins.")
    w = int(input("How many quarters ?"))
    x = int(input("How many dimes ?"))
    y = int(input("How many nickles ?"))
    z = int(input("How many pennies ?"))
    print(amount(w, x, y, z))
    return True

coffee = True
while coffee:
    a = input("What would you like? (espresso/latte/cappuccino):")
    if a == "off":
        coffee = False
        break
    if a == "report":
        print(resources)
        continue
    res()