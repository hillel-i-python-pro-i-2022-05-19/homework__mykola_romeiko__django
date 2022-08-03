import logging

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from apps.user_generator.utils import get_all_users

logger = logging.getLogger(__name__)


def user_generator(request: HttpRequest, quantity: int = 100) -> HttpResponse:
    users = get_all_users(quantity=quantity)
    logger.info(f'list[T_PERSON(name, email)]: {users}')
    return render(request, 'user_generator/show_user.html', {'users': users})
