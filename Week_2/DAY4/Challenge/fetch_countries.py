import requests
import psycopg2

# Database connection
def connect_db():
    return psycopg2.connect(host="localhost", user="postgres", password="test", dbname="ChallengeDAY4")

def create_countries_table(conn):
    with conn.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Countries (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                capital VARCHAR(100) NOT NULL,
                flag VARCHAR(255) NOT NULL,
                subregion VARCHAR(100) NOT NULL,
                population INT NOT NULL
            )
        ''')
        conn.commit()

def fetch_random_countries():
    response = requests.get("https://restcountries.com/v3.1/all")
    if response.status_code == 200:
        countries = response.json()
        return countries
    else:
        print("Error fetching data from API.")
        return []

def save_countries_to_db(countries):
    conn = connect_db()
    create_countries_table(conn)
    with conn.cursor() as cursor:
        count = 0
        for country in countries:
            if count >= 10:
                break
            try:
                name = country["name"]["common"]
                capital = country["capital"][0] if "capital" in country else "N/A"
                flag = country["flags"]["svg"] if "flags" in country else "N/A"
                subregion = country["subregion"] if "subregion" in country else "N/A"
                population = country["population"] if "population" in country else 0

                cursor.execute('''
                    INSERT INTO Countries (name, capital, flag, subregion, population)
                    VALUES (%s, %s, %s, %s, %s)
                ''', (name, capital, flag, subregion, population))
                count += 1
            except Exception as e:
                print(f"An error occurred: {e}")
        conn.commit()
    conn.close()
    print("Data saved successfully.")

if __name__ == "__main__":
    countries = fetch_random_countries()
    save_countries_to_db(countries[:10])  # Select the first 10 countries