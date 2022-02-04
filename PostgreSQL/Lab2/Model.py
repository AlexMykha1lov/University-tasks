import time
import psycopg2


def connect():
    connection = psycopg2.connect(
        database="Library",
        user="postgres",
        password="ndeene28082002",
        host="127.0.0.1")
    connection.autocommit = True
    return connection


def close():
    connection = connect()
    connection.close()


def insert(table, inp):
    connection = connect()
    if table == 1:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Author"(author_id, name, origin) VALUES(%s, %s, %s);""",
                           (inp[0], inp[1], inp[2],))

    elif table == 2:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Book"(book_id, sub_id, author_id, title, genre) 
            VALUES(%s, %s, %s, %s, %s);""",
                           (inp[0], inp[1], inp[2], inp[3], inp[4],))

    elif table == 3:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Subscription"(sub_id, name, email) 
                VALUES(%s, %s, %s);""", (inp[0], inp[1], inp[2],))


def insert_rand(table, count):
    connection = connect()
    if table == 1:
        with connection.cursor() as cursor:

            for i in range(0, count):
                cursor.execute("""INSERT INTO "Author"(author_id, name, origin)
                    VALUES(
                    (SELECT(select count(author_id) from "Author")+1::int),
                    (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int)
                        )),
                    (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int)
                        )));""")

    elif table == 2:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Book"(book_id, sub_id, author_id, title, genre)
                 VALUES(
                 (SELECT(select count(book_id) from "Book")+1::int),
                 (SELECT sub_id FROM "Subscription" OFFSET 
                 floor(random()*(select count(sub_id) from "Subscription")) LIMIT 1),
                 (SELECT author_id FROM "Author" OFFSET 
                 floor(random()*(select count(author_id) from "Author")) LIMIT 1),
                 (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int)
                        )),
                (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int)
                        )));""")

    elif table == 3:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO "Subscription"(sub_id, name, email) 
                 VALUES(
                 (SELECT(select count(sub_id) from "Subscription")+1::int),
                 (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int))),
                (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        '@email.com'
                        ))  
                        );""", )


def update(table, inp):
    connection = connect()

    n_id = inp[0]
    column = inp[1]
    new = inp[2]

    if table == 1:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Author" set name = %s where author_id = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Author" set origin = %s where author_id = %s;""", (new, n_id,))

    elif table == 2:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Book" set sub_id = %s where book_id = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Book" set author_id = %s where book_id = %s;""", (new, n_id,))

        elif column == 3:
            with connection.cursor() as cursor:
                cursor.execute("""update "Book" set title = %s where book_id = %s;""", (new, n_id,))

        elif column == 4:
            with connection.cursor() as cursor:
                cursor.execute("""update "Book" set genre = %s where book_id = %s;""", (new, n_id,))

    elif table == 3:
        if column == 1:
            with connection.cursor() as cursor:
                cursor.execute("""update "Subscription" set name = %s where sub_id = %s;""", (new, n_id,))

        elif column == 2:
            with connection.cursor() as cursor:
                cursor.execute("""update "Subscription" set email = %s where sub_id = %s;""", (new, n_id,))


def delete(table, nid):
    connection = connect()

    if table == 1:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Author" WHERE author_id = %s;""", (nid,))

    elif table == 2:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Book" WHERE book_id = %s;""", (nid,))

    elif table == 3:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE from "Subscription" WHERE sub_id = %s;""", (nid,))


def select_table(table, inp):
    connection = connect()

    string = inp[0]

    if table == 1:
        if string == 1:
            n_id = inp[1]
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Author" where author_id = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Author";""")
                return cursor.fetchall()

    elif table == 2:
        if string == 1:
            n_id = inp[1]
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Book" where book_id = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Book";""")
                return cursor.fetchall()

    elif table == 3:
        if string == 1:
            n_id = inp[1]
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Subscription" where sub_id = %s;""", (n_id,))
                return cursor.fetchmany(1)

        elif string == 2:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Subscription";""")
                return cursor.fetchall()


def search(table, inp):
    connection = connect()

    column = inp[0]

    if table == 1:
        if column == 1:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Author" WHERE %s <= author_id and author_id <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            txt = inp[1]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Author" WHERE
                    to_tsvector(name) || to_tsvector(origin)
                    @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()
                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

    elif table == 2:

        if column == 1:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Book" WHERE %s <= book_id and book_id <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Book" WHERE %s <= sub_id and sub_id <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 3:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Book" WHERE %s <= author_id and author_id <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 4:
            txt = inp[1]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Book" WHERE
                    to_tsvector(title) || to_tsvector(genre)
                    @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

    elif table == 3:
        if column == 1:
            a = inp[1]
            b = inp[2]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Subscription" WHERE %s <= sub_id and sub_id <= %s;""", (a, b,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

        elif column == 2:
            txt = inp[1]
            with connection.cursor() as cursor:
                start = time.time()
                cursor.execute("""SELECT * FROM "Subscription" WHERE to_tsvector(name) || to_tsvector(email)
                    @@ plainto_tsquery(%s);;""", (txt,))
                finish = time.time()

                search_duration = finish - start
                f_a = cursor.fetchall()
                ret = [f_a, search_duration]
                return ret

