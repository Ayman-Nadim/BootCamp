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
        print(f"\nThe {self.last_name} family:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")


class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] < 18:
                    raise Exception(f"{name} is not old enough to use their power!")
                print(f"{member['incredible_name']} uses {member['power']}!")

    def incredible_presentation(self):
        print("\n✨ Here is our powerful family ✨")
        super().family_presentation()  # Call the parent class method
        for member in self.members:
            if "power" in member and "incredible_name" in member:
                print(f"Incredible Name: {member['incredible_name']}, Power: {member['power']}")


incredible_family = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])


incredible_family.incredible_presentation()


incredible_family.born(name="Jack", age=0, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")


incredible_family.incredible_presentation()
