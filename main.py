resources = {
    "bread": 12,  # slice
    "ham": 18,    # slice
    "cheese": 24  # ounces
}
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,    # slice
            "cheese": 4  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slice
            "ham": 6,    # slice
            "cheese": 8  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slice
            "ham": 8,    # slice
            "cheese": 12 # ounces
        },
        "cost": 5.5,
    }
}
def prompt_user():
    return input("What would you like? (small/medium/large/off/report): ").lower()
def check_resources(order):
    ingredients = recipes[order]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coins():
    print("Please insert coins.")
    large_dollars = int(input("how many large dollars?: "))
    half_dollars = int(input("how many half dollars?: "))
    quarters = int(input("how many quarters?: "))
    nickels = int(input("how many nickels?: "))
    total = large_dollars * 1.0 + half_dollars * 0.5 + quarters * 0.25 + nickels * 0.05
    return total
def transaction_result(coins, cost):
    if coins < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif coins > cost:
        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
    return True
def make_sandwich(order):
    ingredients = recipes[order]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"{order} sandwich is ready. Bon appetit!")
def show_report():
    for item in resources:
        print(f"{item.capitalize()}: {resources[item]} slice(s)" if item == "bread" or item == "ham" else f"{item.capitalize()}: {resources[item]} ounce(s)")
while True:
    choice = prompt_user()
    if choice == "off":
        break
    elif choice == "report":
        show_report()
    elif choice in recipes:
        if check_resources(choice):
            payment = process_coins()
            if transaction_result(payment, recipes[choice]["cost"]):
                make_sandwich(choice)
    else:
        print("Invalid choice. Please try again.")
