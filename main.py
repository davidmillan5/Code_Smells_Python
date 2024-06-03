import psycopg2
from models import User
from services.UserService import UserService
from repository.PostgreSQLRepository import PostgreSQLRepository
from controllers.UserControllers import UserController

connection_string = "postgres://djunvgmt:tr4l4n2htIRoNbXMzLSDm-URgPThV_l9@bubble.db.elephantsql.com/djunvgmt"

# Create instances of repository, service, and controller
repository = PostgreSQLRepository(connection_string)
service = UserService(repository)
controller = UserController(service)

try:
    conn = psycopg2.connect(connection_string)
    print("Connection to PostgreSQL database successful!")

    # Perform database operations here

    # Get user by ID
    user_id = 2
    controller.get_user_by_id(user_id)

    # Get all users
    controller.get_all_users()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgresSQL database:", error)
finally:
    # Close the database connection
    if conn:
        conn.close()
        print("Connection closed.")
