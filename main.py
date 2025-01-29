import sqlite3

from functions import connect_db

conn, curser = connect_db("HWSQLPREP11.db")

""" exc.a """
curser.execute("CREATE TABLE category (category_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);")
curser.execute("CREATE TABLE products (product_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price REAL, category_id INTEGER NOT NULL, FOREIGN KEY (category_id) REFERENCES category (category_id));")
curser.execute("CREATE TABLE nutrition (nutrition_id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER NOT NULL, name TEXT NOT NULL, calories INTEGER NOT NULL, fats INTEGER NOT NULL, sugar INTEGER NOT NULL, FOREIGN KEY (product_id) REFERENCES products (product_id));")
curser.execute("CREATE TABLE orders (order_id INTEGER PRIMARY KEY AUTOINCREMENT, date_time TEXT NOT NULL, address TEXT NOT NULL, customer_name TEXT NOT NULL, customer_ph TEXT UNIQUE, total_price REAL NOT NULL);")
curser.execute("CREATE TABLE products_orders (order_id INTEGER NOT NULL, product_id INTEGER NOT NULL, amount INTEGER NOT NULL, FOREIGN KEY (order_id) REFERENCES orders (order_id), FOREIGN KEY (product_id) REFERENCES products (product_id), PRIMARY KEY (order_id, product_id));")

"""exc.b"""
"""

"""

"""exc.c"""
curser.execute("INSERT INTO category (name) VALUES ('Beverages'), ('Snacks'), ('Dairy'), ('Fruits'), ('Vegetables');")
curser.execute("INSERT INTO products (name, price, category_id) VALUES ('Orange Juice', 5.99, 1), ('Chocolate Bar', 2.50, 2), ('Milk', 3.20, 3), ('Apple', 1.50, 4), ('Carrot', 0.99, 5), ('Coca Cola', 1.50, 1),('Pepsi', 1.40, 1), ('Water Bottle', 0.99, 1), ('Orange Soda', 1.70, 1), ('Iced Tea', 2.00, 1), ('Potato Chips', 1.80, 2), ('Pretzels', 2.20, 2), ('Popcorn', 1.99, 2), ('Granola Bar', 1.50, 2), ('Cookies', 3.00, 2), ('Cheese', 4.50, 3), ('Yogurt', 1.25, 3), ('Butter', 3.75, 3), ('Cream Cheese', 2.50, 3), ('Ice Cream', 5.00, 3), ('Banana', 1.20, 4), ('Grapes', 2.99, 4), ('Mango', 1.75, 4), ('Pineapple', 3.00, 4), ('Strawberries', 2.80, 4);")
curser.execute("INSERT INTO nutrition (product_id, name, calories, fats, sugar) VALUES (1, 'Orange Juice', 120, 0.2, 20), (2, 'Chocolate Bar', 220, 12, 18), (3, 'Milk', 150, 8, 12), (4, 'Apple', 95, 0.3, 19), (5, 'Carrot', 41, 0.1, 5), (6, 'Coca Cola', 140, 0, 39), (7, 'Pepsi', 150, 0, 41), (8, 'Water Bottle', 0, 0, 0), (9, 'Orange Soda', 160, 0, 44), (10, 'Iced Tea', 90, 0, 23), (11, 'Potato Chips', 160, 10, 1), (12, 'Pretzels', 110, 1, 1), (13, 'Popcorn', 120, 5, 0), (14, 'Granola Bar', 150, 6, 7), (15, 'Cookies', 250, 12, 18), (16, 'Cheese', 113, 9, 1), (17, 'Yogurt', 80, 1.5, 11), (18, 'Butter', 100, 11, 0), (19, 'Cream Cheese', 99, 10, 1), (20, 'Ice Cream', 270, 14, 28), (21, 'Banana', 105, 0.3, 14), (22, 'Grapes', 62, 0.3, 15), (23, 'Mango', 99, 0.6, 23), (24, 'Pineapple', 50, 0.1, 10), (25, 'Strawberries', 53, 0.5, 8);")
curser.execute("INSERT INTO orders (date_time, address, customer_name, customer_ph, total_price) VALUES ('2024-09-17 10:30', '123 Main St', 'John Doe', '555-1234', 30.08), ('2024-09-17 11:45', '456 Oak St', 'Jane Smith', '555-5678', 20.13), ('2024-09-17 12:15', '789 Pine St', 'Emily Davis', '555-8765', 22.22), ('2024-09-17 13:00', '321 Elm St', 'Michael Johnson', '555-4321', 15.15), ('2024-09-17 13:30', '654 Maple St', 'Sarah Wilson', '555-6789', 30.99);")
curser.execute("INSERT INTO products_orders (order_id, product_id, amount) VALUES (1, 1, 2),(1, 2, 1), (2, 3, 1), (3, 4, 3), (4, 5, 5), (5, 1, 1), (5, 3, 2), (5, 4, 2), (1, 6, 3), (1, 11, 1), (2, 7, 2), (2, 12, 2), (3, 8, 1), (3, 13, 2), (4, 9, 1), (4, 14, 2), (5, 10, 1), (5, 15, 1), (1, 16, 1), (2, 17, 3), (3, 18, 2), (4, 19, 1), (5, 20, 1), (1, 21, 4), (2, 22, 2), (3, 23, 3), (4, 24, 1), (5, 25, 2);")

"""exc.d"""
print([tuple(row) for row in (curser.execute("SELECT category.name AS category_name, products.name AS product_name, nutrition.calories, nutrition.fats, nutrition.sugar FROM category JOIN products ON products.category_id = category.category_id JOIN nutrition ON nutrition.product_id = products.category_id;").fetchall())])
print([tuple(row) for row in (curser.execute("SELECT products_orders.*, products.name AS product_name, products.price FROM products_orders JOIN products ON products.product_id = products_orders.product_id ORDER BY products_orders.order_id;").fetchall())])
curser.execute("INSERT INTO products_orders VALUES (1, 12, 1), (2, 23 , 1), (3, 10 , 1), (4, 6, 1), (5, 8, 1);")
curser.execute("UPDATE orders  SET total_price = tp FROM (SELECT products_orders.order_id AS o_i ,SUM(products_orders.amount)*products.price AS tp from products_orders JOIN products on products_orders.product_id=products.product_id GROUP BY order_id) WHERE orders.order_id= o_i;")
print([tuple(row) for row in (curser.execute("SELECT order_id, MAX(total_price) FROM  orders;").fetchall())])
print([tuple(row) for row in (curser.execute("SELECT order_id, MIN(total_price) FROM  orders;").fetchall())])
print([tuple(row) for row in (curser.execute("SELECT order_id, AVG(total_price) FROM  orders;").fetchall())])
print([tuple(row) for row in (curser.execute("SELECT products_orders.order_id AS customer_id, COUNT(products_orders.order_id) AS total_orders, orders.customer_name FROM products_orders JOIN orders ON orders.order_id = products_orders.order_id GROUP BY products_orders.order_id;").fetchall())])
print([tuple(row) for row in (curser.execute("SELECT products_orders.product_id, SUM(products_orders.amount) AS total_orders, products.name FROM products_orders JOIN products ON products.product_id = products_orders.product_id GROUP BY products_orders.product_id ORDER BY total_orders DESC;").fetchall())])
print([tuple(row) for row in (curser.execute("SELECT products_orders.product_id, SUM(products_orders.amount) AS total_orders, products.name FROM products_ordersJOIN products ON products.product_id = products_orders.product_idGROUP BY products_orders.product_id;").fetchall())])
print([tuple(row) for row in (curser.execute("SELECT products_orders.product_id, SUM(products_orders.amount) AS total_orders, products.name FROM products_orders JOIN products ON products.product_id = products_orders.product_id GROUP BY products_orders.product_id ORDER BY total_orders DESC;").fetchall())])
print([tuple(row) for row in (curser.execute("SELECT category.*,products.product_id, SUM(products_orders.amount ) AS ta FROM category JOIN products ON products.category_id = category.category_id JOIN products_orders ON products_orders.product_id = products.product_id GROUP BY category.category_id ORDER BY  ta DESC;").fetchall())])
print([tuple(row) for row in (curser.execute("SELECT category.*,products.product_id, SUM(products_orders.amount ) AS ta FROM category JOIN products ON products.category_id = category.category_id JOIN products_orders ON products_orders.product_id = products.product_id GROUP BY category.category_id ORDER BY  ta;").fetchall())])




conn.commit()
conn.close()