import uuid

class User:
    email = ""
    username = ""
    first_name = ""
    last_name = ""
    email_user_id = ""
    id = ""

    def __init__(self, email: str, first_name: str, last_name: str) -> None:
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.email_user_id = email
        self.username = email
        self.id = uuid.uuid4()


    def to_json(self) -> str:
        return {
            "email": self.email,
            "username" : self.username,
            "first_name": self.first_name,
            "last_name" : self.last_name,
            "email_user_id" : self.email_user_id,
            "id": self.id
        }