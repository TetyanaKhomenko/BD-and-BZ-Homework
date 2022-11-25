import sqlite3
import data

conn = sqlite3.connect('pt3.db')
c = conn.cursor()

c.execute("""CREATE TABLE words (
                    word_id integer primary key,
                    word text,
                    pos_type varchar
                     )""")

c.execute("""CREATE TABLE pos (
                    pos_type text
                     )""")

c.execute("""CREATE TABLE inflections (
                    word_id integer,
                    inflected_form text,
                    FOREIGN KEY (word_id) REFERENCES words(word_id)
                     )""")
conn.commit()

pos = set([v[0] for v in data.words.values() if v[0] is not None])
for i in pos:
    c.execute("INSERT INTO pos VALUES (?)", (i,))
    conn.commit()
i=1
for k,v in data.words.items():
    c.execute("INSERT INTO words VALUES (?,?,?)", (i, v[0], k))
    for inf in v[1]:
        c.execute("INSERT INTO inflections VALUES (?,?)", (i, inf))
    i += 1
    conn.commit()
