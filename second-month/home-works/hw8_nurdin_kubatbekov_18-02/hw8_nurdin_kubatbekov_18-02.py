import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_product_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
    return conn


def insert_product(conn, product):
    try:
        sql = '''INSERT INTO products
                (product_title, price, quantity)
                VALUES(?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def update_product(conn, product):
    try:
        sql = '''UPDATE products SET
        quantity = ?, price= ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
    except sqlite3.Error as e:
        print(e)


def select_products_by_price_quantity_title(conn, product):
    try:
        sql = '''SELECT * FROM products WHERE price <= ? and quantity >= ? or product_title = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
    except sqlite3.Error as e:
        print(e)


create_product_table_sql = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (10) NOT NULL DEFAULT 0,
)
'''


database = r'home-work.db'

conn = create_connection(database)

if conn is not None:
    print('Connected successfully!')
    create_product_table(conn, create_product_table_sql)
    # insert_product(conn, ('Red-Honey', 583.97, 54321))
    # insert_product(conn, ('Red-Honey1', 583.97, 54321))
    # insert_product(conn, ('Red-Honey2', 583.97, 54321))
    # insert_product(conn, ('Red-Honey3', 583.97, 54321))
    # insert_product(conn, ('Red-Honey4', 583.97, 54321))
    # insert_product(conn, ('Red-Honey5', 583.97, 54321))
    # insert_product(conn, ('Red-Honey6', 583.97, 54321))
    # insert_product(conn, ('Red-Honey7', 583.97, 54321))
    # insert_product(conn, ('Red-Honey8', 583.97, 54321))
    # insert_product(conn, ('Red-Honey9', 583.97, 54321))


    # update_product(conn, (54321, 87453670.34, 2))

    # delete_product(conn, 15)

    # select_all_products(conn)

    # select_products_by_price_quantity_title(conn, (90.00, 10, 'Red-Honey1'))

    conn.close()
else:
    print('ERROR! can create connection to DB ' + database)