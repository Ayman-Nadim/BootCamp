import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

        self.connection = psycopg2.connect(host="localhost", user="postgres", password="test", dbname="DAY4")
        self.cursor = self.connection.cursor()
        print("Database connection established in MenuItem.")

    def save(self):
        
        query = f"INSERT INTO Menu_Items (item_name, item_price) VALUES ('{self.name}', {self.price})"
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print(f"Item '{self.name}' saved successfully.")
        
        except Exception as e:
            print(f"An error occurred while saving the item: {e}")



    def delete(self):
        
        query = f"DELETE FROM Menu_Items WHERE item_name = '{self.name}'"
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print(f"Item '{self.name}' deleted successfully.")
        except Exception as e:
            print(f"An error occurred while deleting the item: {e}")





    def update(self, new_name=None, new_price=None):
        
        updates = []
        if new_name:
            updates.append(f"item_name = '{new_name}'")
        if new_price is not None:  # Check for None to allow price to be set to None
            updates.append(f"item_price = {new_price}")

        if updates:
            update_query = ", ".join(updates)
            query = f"UPDATE Menu_Items SET {update_query} WHERE item_name = '{self.name}'"
            try:
                self.cursor.execute(query)
                self.connection.commit()
                print(f"Item '{self.name}' updated successfully.")
            except Exception as e:
                print(f"An error occurred while updating the item: {e}")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("Database connection closed.")