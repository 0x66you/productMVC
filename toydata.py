import sqlite3

conn = sqlite3.connect('marketplace.db')
c = conn.cursor()

sql = ''' 
INSERT INTO product (id, name, price, quantity, date) 
VALUES (1, 'Elite Series 2 Controller - Black', 148.49, 38, '2018-12-31'),
       (2, 'Nintendo Switch -HAC-001', 264.99, 209, '2019-08-29'),
       (3, 'Razer BlackShark V2 Headset', 99.99, 200, '2020-07-30'),
       (4, 'Kingston 240GB A400 SATA 3', 27.99, 14, '2018-07-01'),
       (5, 'Garmin Forerunner 235', 169.99, 85, '2015-10-21');
'''
c.execute(sql)
conn.commit()
conn.close()