import logging

from django.http import HttpResponse

from apps.user_generator.utils import get_all_users

logger = logging.getLogger(__name__)


def user_generator(request, quantity: int = 100) -> HttpResponse:
    users = get_all_users(quantity=quantity)
    logger.info(f'list[T_PERSON(name, email)]: {users}')
    return HttpResponse(f'<p>{user.name} {user.email}<p>' for user in users)
