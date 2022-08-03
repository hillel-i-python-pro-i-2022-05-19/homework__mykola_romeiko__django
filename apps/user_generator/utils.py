from collections import namedtuple
from typing import NamedTuple, TypeAlias, Iterator

from faker import Faker

T_PERSON: TypeAlias = NamedTuple


def get_all_users(quantity: int) -> list[T_PERSON]:
    return list(generate_users(quantity=quantity))


def generate_users(quantity: int) -> Iterator[T_PERSON]:
    """
    by quantity param
    :return: list with generated namedtuple objects(example: Person(name='John', email='john@gmail.com'))
    """
    fake = Faker('en_US')
    Faker.seed(fake.random.randint(0, 9999))
    for _ in range(quantity):
        yield generate_user(fake)


def generate_user(fake: Faker) -> T_PERSON:
    Person = namedtuple('Person', {'name', 'email'})
    return Person(name=fake.profile()['name'].split()[0], email=fake.profile()['mail'])
