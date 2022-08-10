import sqlite3

def main(lst):
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()

    # create a table tab_text, tab_num
    cursor.execute(""" CREATE TABLE IF NOT EXISTS tab_text(data_text TEXT);""")
    cursor.execute(""" CREATE TABLE IF NOT EXISTS tab_num(data_num INT);""")
    conn.commit()

    for i in lst:
        if type(i) == str:
            length = len(i)
            query = '''INSERT INTO tab_text (data_text) VALUES (?)'''
            cursor.execute(query, (i,))
            query = '''INSERT INTO tab_num (data_num) VALUES (?)'''
            cursor.execute(query, (length,))           
            conn.commit()

        elif type(i) == int:
            if i % 2 == 0:
                query = '''INSERT INTO tab_num (data_num) VALUES (?)'''
                cursor.execute(query, (i,))
                conn.commit()                         
            else:
                query = '''INSERT INTO tab_text (data_text) VALUES (?)'''
                cursor.execute(query, ('нечетное',))
                conn.commit()

    cursor.execute('''SELECT * FROM tab_num''')
    res = len([row for row in cursor])

    if res > 5:
        cursor.execute(''' SELECT * FROM tab_text LIMIT 1 ''')
        record = cursor.fetchone()
        cursor.execute(''' DELETE FROM tab_text WHERE data_text = ? ''', record)
    elif res < 5:
        cursor.execute(''' SELECT * FROM tab_text LIMIT 1 ''')
        record = cursor.fetchone()
        cursor.execute('''UPDATE tab_text SET data_text = "hello" WHERE data_text = ? ''', record)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    lst = ['hello', 'sample', 256, 17, 48, 'Ruby', 'Python', 18, 27, 'Go']    
    main(lst)
