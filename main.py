import sqlite3

from functions import connect_db

conn, curser = connect_db("HWSQLPREP11.db")

curser.execute("CREATE TABLE category (category_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
curser.execute("CREATE TABLE products (product_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER, category_id INTEGER, FOREIGN KEY (category_id) REFERENCES category (category_id))")
curser.execute("CREATE TABLE nutrition (nutrition_id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER, name TEXT, calories INTEGER, fats INTEGER, sugar INTEGER, FOREIGN KEY (product_id) REFERENCES products (product_id))")
curser.execute("CREATE TABLE orders (order_id INTEGER PRIMARY KEY AUTOINCREMENT, date_time TEXT, address TEXT, customer_name TEXT, customer_ph TEXT, total_price INTEGER)")
curser.execute("CREATE TABLE products_orders (order_id INTEGER, product_id INTEGER, amount INTEGER, FOREIGN KEY (order_id) REFERENCES orders (order_id), FOREIGN KEY (product_id) REFERENCES products (product_id), PRIMARY KEY (order_id, product_id))")


conn.commit()
conn.close()