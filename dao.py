# DAO (Data Access Object) 資料存取物件
import sqlite3

from model import Product


class Dao:

    def __init__(self):
        self.conn = None
        self.c = None

    def connect_db(self):
        self.conn = sqlite3.connect('marketplace.db')
        self.c = self.conn.cursor()

    def disconnect_db(self):
        self.conn.close()

    def add_data(self, product: Product):
        sql = f"""
         INSERT INTO product (id,name,quantity,price,date)
         VALUES({product.id_},'{product.name_}','{product.quantity_}','{product.price_}','{product.date_}')
         """
        self.c.execute(sql)
        self.conn.commit()

    def search_all(self):
        sql = 'SELECT * FROM product'
        self.c.execute(sql)
        self.conn.commit()
        return self.c.fetchall()

    def search_id(self, id_: int):
        sql = f'SELECT * FROM product WHERE id={id_}'
        self.c.execute(sql)
        self.conn.commit()
        return self.c.fetchall()

    def delete_all(self):
        sql = f'DELETE FROM product'
        self.c.execute(sql)
        self.conn.commit()
        # rowcount 代表 sql 操作完成的資料筆數
        if self.c.rowcount > 0:
            return True
        else:
            return False

    def delete_id(self, id_: int):
        sql = f'DELETE FROM product WHERE id={id_}'
        self.c.execute(sql)
        self.conn.commit()
        get_ = self.c.rowcount
        if get_ == 1:
            return True
        else:
            return False

    def update_id(self, data: tuple):
        # data[0] -> id
        # data[1] -> price
        # data[2] -> quantity
        if data[1] and data[2]:
            sql = f'UPDATE product SET price={(data[1])}, quantity={(data[2])} WHERE id={data[0]};'
        elif data[1]:
            sql = f'UPDATE product SET price={(data[1])} WHERE id={data[0]};'
        elif data[2]:
            sql = f'UPDATE product SET quantity={(data[2])} WHERE id={data[0]};'
        else:
            return False
        self.c.execute(sql)
        self.conn.commit()
        return True
