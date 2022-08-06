import logging
import os
import subprocess
from os.path import exists


def check_file_exists(file_path: str) -> bool:
    return exists(file_path)


def create_superuser(username: str, password: str) -> bool:
    try:
        os.environ['DJANGO_SUPERUSER_PASSWORD'] = password
        subprocess.run(['python', 'manage.py', 'createsuperuser', '--username', f'{username}', '--email', 'admin@gmail.com', '--noinput'])
        logging.info(msg=f'Superuser was created(username - {username}, password - {password}).')
        return True
    except Exception as e:
        logging.exception(msg=e)
        return False


if __name__ == '__main__':
    if not check_file_exists('../db/db.sqlite3'):
        create_superuser(username='admin', password='admin')
