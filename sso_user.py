import uuid
from faker import Faker


fake = Faker(["en-GB"])


class User:
    def __init__(self, email: str = None, first_name: str = None, last_name: str = None) -> None:

        self.email = email if email else fake.email()
        self.first_name = first_name if first_name else fake.first_name()
        self.last_name = last_name if last_name else fake.last_name()
        self.email_user_id = self.email
        self.id = uuid.uuid4()

    def to_json(self) -> str:
        return {
            "email": self.email,
            "contact_email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email_user_id": self.email_user_id,
            "id": self.id,
            "related_emails": [],
            "groups": [],
            "permitted_applications": [],
            "access_profiles": [],
        }
