sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", 
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", 
                   "Pastrami sandwich"];

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []



while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich.lower()}")
    finished_sandwiches.append(sandwich)