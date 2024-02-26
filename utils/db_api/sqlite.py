import sqlite3
from unittest import result


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

# ----------------- Firdavs Programmer ---------------------- #

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

# ----------------- Firdavs Programmer ---------------------- #
    
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

# ----------------- Firdavs Programmer ---------------------- #
#Users jadvali bilan ishlash

    # Foydalanuvchi qo'shish
    def add_user(self, user_id: int, user_fullname: str, username: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"
        result = self.execute(
            sql = "INSERT INTO Users(user_id, user_fullname, username) VALUES(?, ?, ?)",
            parameters=(user_id, user_fullname, username,),
            commit = True
        )
        return result

    # Hamma foydalanuvchilarning id raqamini olish
    def id_users(self):
        result = self.execute(
            sql = "SELECT id FROM Users",
            fetchall = True
        )
        return result


    # Hamma foydalanuvchilarni belgilab ular haqida malumot olish
    def select_all_users(self):
        result = self.execute(
            sql = "SELECT * FROM Users",
            fetchall = True
        )
        return result

    # id bilan bazani tekshirish ya'ni u id bazada bormi yo'qmi
    # Foydalanuvchini tekshirish bazada bor yoki yo'qligini
    def check_user(self, user_id):
        result = self.execute(
            sql = "SELECT user_id FROM Users WHERE user_id=?",
            parameters=(user_id,),
            fetchall=True
        )
        return result

    # Bazadagi foydalanuvchilarni sanash 
    def count_users(self):
        result = self.execute(
            sql = "SELECT COUNT(*) FROM Users",
            fetchone = True,
        )
        return result

    # Users jadvalidagi barcha malumotlarni tozalash          
    def delete_all_users(self):                                 
        result = self.execute(                                
            sql = "DELETE FROM Users WHERE TRUE",             
            commit = True
        )
        return result
# ----------------- Firdavs Programmer ---------------------- #


def logger(statement):
    print(f"Executing: {statement}")


#  _  __ _
# | |/ /(_) _ __    __ _  ___
# | ' / | || '_ \  / _` |/ __|
# | . \ | || | | || (_| |\__ \
# |_|\_\|_||_| |_| \__, ||___/
#                  |___/

#          __
#   ___   / _|
#  / _ \ | |_
# | (_) ||  _|
#  \___/ |_|


#  ____          _    _
# |  _ \  _   _ | |_ | |__    ___   _ __
# | |_) || | | || __|| '_ \  / _ \ | '_ \
# |  __/ | |_| || |_ | | | || (_) || | | |
# |_|     \__, | \__||_| |_| \___/ |_| |_|
#         |___/

#  _                          _  _
# | | __  __ _  _ __    __ _ | |(_)  __ _   __ _
# | |/ / / _` || '_ \  / _` || || | / _` | / _` |
# |   < | (_| || | | || (_| || || || (_| || (_| |
# |_|\_\ \__,_||_| |_| \__,_||_||_| \__, | \__,_|
#                                   |___/

#         _
#   ___  | |__   _   _  _ __    __ _
#  / _ \ | '_ \ | | | || '_ \  / _` |
# | (_) || |_) || |_| || | | || (_| |
#  \___/ |_.__/  \__,_||_| |_| \__,_|


#  _             _  _  _
# | |__    ___  ( )| |(_) _ __    __ _
# | '_ \  / _ \ |/ | || || '_ \  / _` |
# | |_) || (_) |   | || || | | || (_| |
# |_.__/  \___/    |_||_||_| |_| \__, |
#                                |___/
