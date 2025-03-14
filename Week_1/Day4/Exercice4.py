class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members else []

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! A new child, {kwargs['name']}, has been born into the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
        return False  

    def family_presentation(self):
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")

my_family = Family("Smith", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])


my_family.born(name="Emma", age=0, gender="Female", is_child=True)


print(my_family.is_18("Michael"))  
print(my_family.is_18("Emma"))    


my_family.family_presentation()
