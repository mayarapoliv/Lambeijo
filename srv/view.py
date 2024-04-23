from srv.database import LambeijosDB


class View:
    def __init__(self):
        self.db = LambeijosDB()

    def auth_validation(self, user, password):
        id = self.db.user_exists(user)
        if id:
            senha = self.db.validate_password(id)
            if password == senha:
                return id

        return False


    def get_all_cliente_from_id(self, id):
        return self.db.select_client_from_id(str(id))