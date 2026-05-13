from dataclasses import dataclass
from faker import Faker
import time

fake = Faker()


@dataclass
class User:
    login: str
    password: str
    email: str
    full_name: str

def generate_user():

    timestamp = int(time.time())

    login = f"testuser_{timestamp}"

    return User(
        login = login,
        
        password=fake.password(
            length=12,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True
        ),

        email=f"{login}@testmail.com",

        full_name=f"{fake.first_name()} "
                  f"{fake.first_name()} "
                  f"{fake.last_name()}"
    )
    