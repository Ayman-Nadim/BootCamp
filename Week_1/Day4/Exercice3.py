import random
from Exercice2 import Dog  

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False  

    def train(self):
        print(self.bark())  
        self.trained = True 

    def play(self, *dog_names):
        all_dogs = ", ".join(dog_names)
        print(f"{all_dogs} all play together.")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            print(random.choice(tricks))  # Pick a random trick
        else:
            print(f"{self.name} is not trained yet and refuses to do a trick.")


if __name__ == "__main__":
    pet1 = PetDog("Buddy", 4, 18)
    pet2 = PetDog("Charlie", 3, 22)
    pet3 = PetDog("Luna", 2, 15)

    pet1.train() 
    pet1.do_a_trick()  

    pet2.play("Buddy", "Luna") 
