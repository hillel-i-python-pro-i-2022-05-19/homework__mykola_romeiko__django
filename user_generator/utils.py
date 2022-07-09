from collections import namedtuple
from typing import NamedTuple

from faker import Faker


def generate_users(quantity: int) -> list:
    """
    by quantity param
    :return: list with generated namedtuple objects(example: Person(name='John', email='john@gmail.com'))
    """
    fake = Faker('en_US')
    Faker.seed(fake.random.randint(0, 9999))
    return [generate_user(fake) for _ in range(quantity)]


def generate_user(fake: Faker) -> NamedTuple:
    Person = namedtuple('Person', {'name', 'email'})
    return Person(fake.profile()['name'].split()[0], fake.profile()['mail'])
