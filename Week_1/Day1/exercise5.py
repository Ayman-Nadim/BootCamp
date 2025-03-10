my_fav_numbers = {3, 7, 42}
my_fav_numbers.update({9, 12})
print(my_fav_numbers);
my_fav_numbers.remove(max(my_fav_numbers)) ;
print(my_fav_numbers);
friend_fav_numbers = {5, 8, 42}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)