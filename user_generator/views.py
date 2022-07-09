from django.http import HttpResponse

from user_generator.utils import generate_users


def user_generator(request, quantity: int = 100) -> HttpResponse:
    users = generate_users(quantity=quantity)
    return HttpResponse(f'<p>{user.name} {user.email}<p>' for user in users)
