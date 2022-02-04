def start_menu():
    sm = int(input("_______________________\n"
                   "|  1 to insert        |\n"
                   "|  2 to insert random |\n"
                   "|  3 to update        |\n"
                   "|  4 to delete        |\n"
                   "|  5 to select table  |\n"
                   "|  6 to search        |\n"
                   "|  7 to end           |\n"
                   "-----------------------\n"
                   "Input: "))
    if sm < 1 or sm > 7:
        err()
        start_menu()
    else:
        return sm


def tables():
    choice_table = int(input("_______________________\n"
                             "| Select a table:     |\n"
                             "|    1 = Author       |\n"
                             "|    2 = Book         |\n"
                             "|    3 = Subscription |\n"
                             "-----------------------\n"
                             "Input: "))
    if choice_table < 1 or choice_table > 3:
        err()
        tables()
    else:
        return choice_table


def input_insert(table):
    if table == 1:
        id_a = int(input("Input new author_id: "))
        name = str(input("Input new author name: "))
        origin = str(input("Input new origin: "))

        inp = [id_a, name, origin]
        return inp

    elif table == 2:
        id_b = int(input("Input new book id: "))
        id_s = int(input("Input new sub id: "))
        id_a = int(input("Input new author id: "))
        title = str(input("Input new title: "))
        ganre = str(input("Input new ganre: "))

        inp = [id_b, id_s, id_a, title, ganre]
        return inp

    elif table == 3:
        id_s = int(input("Input new sub id: "))
        name = str(input("Input new name: "))
        email = str(input("Input new email: "))

        inp = [id_s, name, email]
        return inp


def count_rand():
    count = int(input("Input amount of data to generate: "))
    return count


def input_update(table):
    new = None
    if table == 1:
        id_a = int(input("Num of author id: "))
        column = int(input("1 = to upd name\n"
                           "2 = to upd origin\n"
                           "Input:"))
        if column == 1:
            new = str(input("New author name: "))
        elif column == 2:
            new = str(input("New origin: "))
        else:
            err()
            input_update(table)

        inp = [id_a, column, new]
        return inp

    elif table == 2:
        id_b = int(input("Num of book id: "))
        column = int(input("1 = to upd sub id\n"
                           "2 = to upd author id\n"
                           "3 = to upd title\n"
                           "4 = to upd ganre\n"
                           "Input:"))
        if column == 1:
            new = int(input("New sub id: "))
        elif column == 2:
            new = int(input("New author id: "))
        elif column == 3:
            new = str(input("New title: "))
        elif column == 4:
            new = str(input("New ganre: "))
        else:
            err()
            input_update(table)

        inp = [id_b, column, new]
        return inp

    elif table == 3:
        id_s = int(input("Num of id: "))
        column = int(input("1 = to upd name\n"
                           "2 = to upd email\n"
                           "Input:"))
        if column == 1:
            new = str(input("New name: "))
        elif column == 2:
            new = str(input("New email: "))
        else:
            err()
            input_update(table)

        inp = [id_s, column, new]
        return inp


def del_id():
    nid = int(input("Num of id: "))
    return nid


def input_select():
    string = int(input("1 = to one str\n"
                       "2 = to all str\n"
                       "Input:"))
    if string == 1:
        nid = int(input("Num of id: "))
        inp = [string, nid]
        return inp

    elif string == 2:
        inp = [string]
        return inp

    else:
        err()
        input_select()


def input_search(table):
    if table == 1:
        column = int(input("1 = to search author_id\n"
                           "2 = to search name\n"
                           "3 = to search origin\n"
                           "Input:"))
        if column == 1:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp

        elif column == 2 or column == 3:
            txt = str(input("Input text: "))
            inp = [column, txt]
            return inp

        else:
            err()
            input_search(table)

    elif table == 2:
        column = int(input("1 = to search book_id\n"
                           "2 = to search sub_id\n"
                           "3 = to search author_id\n"
                           "4 = to search title\n"
                           "5 = to search genre\n"

                           "Input:"))
        if column == 1 or column == 2 or column == 3:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp

        elif column == 4 or column == 5:
            txt = str(input("Input text: "))
            inp = [column, txt]
            return inp

        else:
            err()
            input_search(table)

    elif table == 3:
        column = int(input("1 = to search sub_id\n"
                           "2 = to search name\n"
                           "3 = to search email\n"

                           "Input:"))
        if column == 1:
            a = int(input("Input start: "))
            b = int(input("Input finish: "))
            inp = [column, a, b]
            return inp

        elif column == 2 or column == 3:
            txt = str(input("Input text: "))
            inp = [column, txt]
            return inp

        else:
            err()
            input_search(table)


def fetch(table, f_table, inp):
    if table == 1:
        if inp[0] == 1:
            print("\nname =", f_table[0])
            print("origin =", f_table[1], "\n")
        elif inp[0] == 2:
            for i in f_table:
                print("\n""author_id =", i.author_id)
                print("name =", i.name)
                print("origin =", i.origin, "\n")
    elif table == 2:
        if inp[0] == 1:
            print("\nsub_id =", f_table[0])
            print("author_id =", f_table[1])
            print("title =", f_table[2])
            print("genre =", f_table[3], "\n")
        elif inp[0] == 2:
            for i in f_table:
                print("\n""book_id =", i.book_id)
                print("sub_id =", i.sub_id)
                print("author_id =", i.author_id)
                print("title =", i.title)
                print("genre =", i.genre, "\n")
    elif table == 3:
        if inp[0] == 1:
            print("\nname =", f_table[0])
            print("email =", f_table[1], "\n")
        elif inp[0] == 2:
            for i in f_table:
                print("\n""sub_id =", i.sub_id)
                print("name =", i.name)
                print("email =", i.email, "\n")


def data(task):
    if task == 1:
        print("\n[Data was successfully inserted]\n")
    elif task == 2:
        print("\n[Random Data was successfully inserted]\n")
    elif task == 3:
        print("\n[Data was successfully updated]\n")
    elif task == 4:
        print("\n[Data was successfully deleted]\n")


def search_time(t):
    print("\nSearch duration = ", t, "\n")


def err():
    print("\n[Error input, try again!]\n")


def print_close():
    print("[PostgreSQL connection closed]")


def err_except(_ex):
    print("\n[Error while working with PostgreSQL", _ex, "]\n")
