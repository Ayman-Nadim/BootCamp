class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(cats):
    return max(cats, key=lambda cat: cat.age)

cat1 = Cat("Whiskers", 5)
cat2 = Cat("Fluffy", 8)
cat3 = Cat("Mittens", 3)

oldest_cat = find_oldest_cat([cat1, cat2, cat3])

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")