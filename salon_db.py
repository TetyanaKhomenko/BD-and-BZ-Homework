import sqlite3
from clients_class import *

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE clients (
                    client_id integer primary key,
                    name text,
                    surname text,
                    gender text
                     )""")

c.execute("""CREATE TABLE av_services (
                    avser_id integer primary key,
                    service_name text,
                    time integer
                     )""")

c.execute("""CREATE TABLE masters (
                    master_id integer primary key ,
                    master_name text,
                    level text 
                     )""")

c.execute("""CREATE TABLE price (
                    price_id integer primary key,
                    master_id integer,
                    avser_id integer,
                    FOREIGN KEY (master_id) REFERENCES masters(master_id),
                    FOREIGN KEY (avser_id) REFERENCES av_services(avser_id)
                     )""")

c.execute("""CREATE TABLE given_service (
                    price_id integer,
                    client_id integer,
                    FOREIGN KEY (price_id) REFERENCES price(price_id),
                    FOREIGN KEY (client_id) REFERENCES clients(client_id)
                     )""")

def ins_client(client):
    with conn:
        c.execute("INSERT INTO clients VALUES (:client_id, :name, :surname, :gender)", {'client_id':client.client_id,'name': client.name, 'surname': client.surname, 'gender': client.gender})

def ins_avser(avser):
    with conn:
        c.execute("INSERT INTO av_services VALUES (:avser_id, :service_name, :time)", {'avser_id': avser.avser_id, 'service_name': avser.service_name, 'time': avser.time})
    
def ins_master(master):
    with conn:
        c.execute("INSERT INTO masters VALUES (:master_id, :master_name, :level)", {'master_id': master.master_id, 'master_name': master.master_name, 'level': master.level})
        
def ins_price(price):
    with conn:
            c.execute("INSERT INTO price VALUES (:price_id,:master_id,:avser_id)", {
                'price_id': price.price_id, 'master_id': price.master_id, 'avser_id': price.avser_id})

# def given_service():
#     with conn:
#         c.execute("INSERT INTO given_service VALUES (:price_id,:client_id)", {
#             'price_id': , 'client_id':})

client_1 = Clients(1,'Mary','Smith','f')
client_2 = Clients(2,'Ivan', 'Petrenko', 'm')
client_3 = Clients(3, 'Kim', 'Kardashian', 'f')
ins_client(client_1)
ins_client(client_2)
ins_client(client_3)

avser_1 =Available_services(1,'manicure', 2)
avser_2 =Available_services(2,'pedicure', 3)
avser_3 = Available_services(3, 'haircut', 1)
ins_avser(avser_1)
ins_avser(avser_2)
ins_avser(avser_3)

master_1 = Masters(1, 'Alina', 'ordinary')
master_2 = Masters(2, 'Kate', 'top')
ins_master(master_1)
ins_master(master_2)

price_1 =Price(1,master_1,1)
price_2 = Price(2,master_1,2)
price_3=Price(3,master_2,3)
ins_price(price_1)
ins_price(price_2)
ins_price(price_3)

c.execute("SELECT price.price_id, masters.master_name, av_services.service_name FROM price, masters, av_services WHERE price.master_id = masters.master_id AND price.avser_id = av_services.avser_id")
c.execute("UPDATE masters SET master_name = 'Olha' , level = 'top' WHERE master_id = 1")
c.execute("SELECT * FROM masters")
print(c.fetchall())
conn.close()