import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

def prompt_user():
    return input("What would you like? (small/medium/large/off/report): ").lower()

def show_report(resources):
    for item, amount in resources.items():
        unit = "slices" if item in ["bread", "ham"] else "ounces"
        print(f"{item.capitalize()}: {amount} {unit}")




def main():
    resources = data.resources
    recipes = data.recipes
    sandwich_maker = SandwichMaker(resources)
    cashier_instance = cashier_instance()

    while True:
        choice = prompt_user()
        
        if choice == "off":
            break
        elif choice == "report":
            show_report(resources)
        elif choice in recipes:
            recipe = recipes[choice]
            ingredients = recipe["ingredients"]
            cost = recipe["cost"]

            if sandwich_maker.check_resources(ingredients):
                payment = cashier_instance.process_coins()
                
                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker.make_sandwich(ingredients)
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()
