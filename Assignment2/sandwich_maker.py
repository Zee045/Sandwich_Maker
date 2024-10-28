
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        """Checks if resources are sufficient for the order."""
        for item, amount in ingredients.items():
            if amount > self.resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deducts the required ingredients from resources and confirms sandwich preparation."""
        for item, amount in ingredients.items():
            self.resources[item] -= amount
        print("Your sandwich is ready. Bon appétit!")
