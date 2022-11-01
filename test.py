import sqlite3  # імпортуємо бібліотеку sqlite3 в проект
conn = sqlite3.connect('b_book.db')#створюємо об’єкт conn(екзампляр класу Connection), необхідний для взаємодії з базою даних, яка міститься в файлі b_book.bd
c = conn.cursor()  # за допомогою метода cursor(), що належить об’єкту conn, створюємо керувальну стркутуру (посередник між бд та запитами) cursor, за доп. якого можна здійснювати запити до бази даних

#за доп. методу execute() виконуємо запит CREATE TABLE, що створює у бд табличку tAuth з атрибутами  AuthorId (тип даних - integer, primary key), AuthorFirstN(тд - текст), AuthorLastN (тп - текст), AuthorAge(тд - число)
c.execute("""CREATE TABLE tAuth (
                    AuthorId integer primary key,
                    AuthorFirstN text,
                    AuthorLastN text,
                    AuthorAge integer
                     )""")

#виконуємо запит INSERT, що вставляє у таблицю firsttable значення атрибутів
c.execute('''INSERT INTO tAuth VALUES (1, "Коріандр","Кравченко",45)''')
c.execute('''INSERT INTO tAuth VALUES (2, "Сидр","Грушевський",33)''')
c.execute('''INSERT INTO tAuth VALUES (3, "Кадр","Фітільов",35)''')
c.execute('''INSERT INTO tAuth VALUES (4, "Ангеліна","Турій",15)''')
c.execute('''INSERT INTO tAuth VALUES (5, "Жанна","Сидор",55)''')

conn.commit()  # для коректного завершення роботи з бд, застосовуємо зміни; робимо це за доп. об’єкта conn і його метода commit()

#5 виводимо  всі таблиці у створеній БД “b_book”
#виводимо назви усіх таблиць, наявних в БД, використовуючи внутрішню таблицю БД sqlite_master, яка описує схему БД; з sqlite_master обираємо всі назви об'єктів типу table
sql_query = """SELECT name FROM sqlite_master  
   WHERE type='table'"""
c.execute(sql_query)
print(c.fetchall())
#виводимо таблиці зі значеннями
#перебираємо (проходимось по) рядки, отримані в результаті виконання запиту SELECT *, що отримує всі значення таблиці tAuth; порядково виводимо результат в консоль
for row in c.execute('SELECT * FROM tAuth'):
    print(row)

#6 виводимо інформацію про те, скільки є записів рядків у "tAuth", використовуючи ф-ію COUNT(*), що повертає кількість усіх рядків, також враховуючи значення NULL та дублікати 
c.execute("SELECT COUNT(*) FROM tAuth")
print(c.fetchall())

#7  виводимо вибірку з "tAuth" дані, попередньо по AuthorId відсортувавши їх за зростанням (asc)
c.execute("SELECT * FROM tAuth ORDER BY AuthorId ASC")
print(c.fetchall())

#8 виводимо вибірку з "tAuth" такого запису AuthorAge, значення якого - найбільше, використовуючи функцію MAX()
c.execute("SELECT MAX(AuthorAge) FROM tAuth")
print(c.fetchall())

#9 виводимо вибірку з "tAuth" записи AuthorFirstName в яких автори закінчуються на "др", використовуючи умову LIKE - в лапках записуємо умову (% - набір символів, з яких два останні -др)
c.execute(''' SELECT * FROM tAuth WHERE AuthorFirstN LIKE "%др" ''')
print(c.fetchall())

#10 додаємо ще два рядки в таблицю
c.execute('''INSERT INTO tAuth VALUES (6, "Ганна","Крушельницька",34)''')
c.execute('''INSERT INTO tAuth VALUES (7, "Ліза","Суворова",27)''')

#11 вносимо зміни в таблицю,  для третього запису(AuthorId=3) змінюємо значення полів прізвища та віку автора, використовуючи запит UPDATE
c.execute("UPDATE tAuth SET AuthorLastN = 'Завгородній',AuthorAge = 19 WHERE AuthorId = 3")
c.execute("SELECT * FROM tAuth")
print(c.fetchall())
conn.close()
