import dramatiq
from django.contrib.auth.models import User


@dramatiq.actor
def add(x, y):
    return x + y


@dramatiq.actor
def create_user(username, email, password):
    User.objects.create_user(username=username, email=email, password=password)


@dramatiq.actor
def user_update_email(user_id, email):
    user = User.objects.get(id=user_id)
    user.email = email
    user.save(update_fields=["email"])
