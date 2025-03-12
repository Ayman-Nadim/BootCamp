def get_random_temp(season):
    ranges = {
        "winter": (-10, 16),
        "spring": (10, 25),
        "summer": (20, 40),
        "autumn": (5, 20)
    }
    return round(random.uniform(*ranges.get(season, (-10, 40))), 1)

def main():
    season = input("Enter season: ").lower()
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp}°C.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp < 23:
        print("Mild weather today.")
    elif temp < 32:
        print("It's warm outside!")
    else:
        print("It's really hot! Stay hydrated.")
main()