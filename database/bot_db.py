import sqlite3
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()


    if db:
        print("База данных подключена!")

    cursor.execute("CREATE TABLE IF NOT EXISTS mentors "
                   "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "fullname TEXT,"
                   "direction TEXT,"
                   "age INTEGER,"
                   "gruppa)")
    db.commit()
    print("Таблица создана!")


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute(
             "INSERT INTO mentors"
            "(fullname, direction, age, gruppa)"
            "VALUES (?, ?, ?, ?)",
            tuple(data.values()))

        db.commit()

async def sql_command_random():
    users = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(users)
    return random_user

async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()