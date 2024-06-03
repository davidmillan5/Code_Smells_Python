from services.UserService import UserService

class UserController:
    def __init__(self, service: UserService):
        self.service = service

    def get_user_by_id(self, user_id):
        user = self.service.get_user_by_id(user_id)
        if user:
            print(f"User found: {user.name}, {user.email}")
        else:
            print("User not found.")

    def get_all_users(self):
        all_users = self.service.get_all_users()
        if all_users:
            print("All Users:")
            for user in all_users:
                print(f"User ID: {user.user_id}, Name: {user.name}, Email: {user.email}")
        else:
            print("No users found.")
