from repository.UserRepository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user_by_id(self, user_id):
        return self.repository.get_user_by_id(user_id)

    def get_all_users(self):
        all_users = self.repository.get_all_users()
        return all_users if all_users is not None else []