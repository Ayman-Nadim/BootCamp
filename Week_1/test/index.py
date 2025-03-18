# etudiants = {
#     "Alice": {"âge": 25, "ville": "Paris"},
#     "Bob": {"âge": 22, "ville": "Lyon"}
# }
# print(etudiants["Alice"]["âge"])  
# mon_dict = dict(nom="Alice", âge=25, ville="Paris")
# print(mon_dict.get("pays", "Non spécifié"))  # Non spécifié
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)