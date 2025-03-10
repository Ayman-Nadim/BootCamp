my_name = "Ayman";  
user_name = input("Quel est votre nom ? ")
if user_name.lower() == my_name.lower():
    print("Nous avons le même nom !")
else:
    print(f"Sympa de vous rencontrer, {user_name} ! Mon nom est {my_name}.")