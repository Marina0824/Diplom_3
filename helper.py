import faker
import random
import string
import requests
from urls import *


def create_email():
    fake = faker.Faker()
    name = "user"
    random_digits = random.randint(1000, 9999)
    domain = fake.free_email_domain()
    email = f"{name}{random_digits}@{domain}"
    return email

def create_password():
    random_digits = random.randint(100000, 999999)
    password = f"{random_digits}"
    return password

def create_name(length):
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(length))
    return name

# создание пользователя по API
def create_new_user():
    email = create_email()
    password = create_password()
    name = create_name(5)
    body = {"email": email,
            "password": password,
            "name": name}
    response = requests.post(f"{URL}{registration}", json=body)
    response_body = response.json()
    token = response_body["accessToken"]
    return email, password, token

#Удаление пользователя по API
def delete_user(token):
    response_delete = requests.delete(f"{URL}{delete}", headers={"Authorization": token})
    return response_delete
