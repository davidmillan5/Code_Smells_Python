import psycopg2
from repository.UserRepository import UserRepository
from models import User


class PostgreSQLRepository(UserRepository):
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_user_by_id(self, user_id):
        global conn, cursor
        try:
            conn = psycopg2.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM "public"."users" WHERE user_id = %s', (user_id,))
            user_data = cursor.fetchone()
            if user_data:
                user = User(user_data[0], user_data[1], user_data[2])
                return user
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgresSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def get_all_users(self):
        global conn, cursor
        try:
            conn = psycopg2.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM "public"."users"')
            users_data = cursor.fetchall()
            users = []
            for user_data in users_data:
                user = User(user_data[0], user_data[1], user_data[2])
                users.append(user)
            return users
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgresSQL", error)
            return []  # Return an empty list if an error occurs
        finally:
            if conn:
                cursor.close()
                conn.close()
