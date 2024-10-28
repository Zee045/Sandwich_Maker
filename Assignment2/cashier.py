class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        """Calculates the total from inserted coins."""
        print("Please insert coins.")
        large_dollars = int(input("How many large dollars?: ")) * 1.0
        half_dollars = int(input("How many half dollars?: ")) * 0.5
        quarters = int(input("How many quarters?: ")) * 0.25
        nickels = int(input("How many nickels?: ")) * 0.05
        return large_dollars + half_dollars + quarters + nickels

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        """Checks if payment is sufficient and returns change if necessary."""
        if total_inserted < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif total_inserted > cost:
            change = round(total_inserted - cost, 2)
            print(f"Here is ${change} in change.")
        return True
