from Model import *
from View import *


def menu():
    task = start_menu()

    if task == 1:
        table = tables()
        inp = input_insert(table)
        try:
            insert(table, inp)
        except Exception as _ex:
            err_except(_ex)
        data(task)

    elif task == 2:
        table = tables()
        if table == 1:
            count = count_rand()
            try:
                insert_rand(table, count)
            except Exception as _ex:
                err_except(_ex)
        else:
            try:
                insert_rand(table, None)
            except Exception as _ex:
                err_except(_ex)
        data(task)

    elif task == 3:
        table = tables()
        inp = input_update(table)
        try:
            update(table, inp)
        except Exception as _ex:
            err_except(_ex)
        data(task)

    elif task == 4:
        table = tables()
        n_id = del_id()
        try:
            delete(table, n_id)
        except Exception as _ex:
            err_except(_ex)
        data(task)

    elif task == 5:
        table = tables()
        inp = input_select()

        try:
            f_t = select_table(table, inp)
            fetch(table, f_t)
        except Exception as _ex:
            err_except(_ex)

    elif task == 6:
        table = tables()
        inp = input_search(table)
        try:
            f_t = search(table, inp)
            fetch(table, f_t[0])
            search_time(f_t[1])
        except Exception as _ex:
            err_except(_ex)

    elif task == 7:
        close()
        print_close()
        return None

    menu()
