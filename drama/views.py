from django.shortcuts import render
from .tasks import add, create_user, user_update_email
from django.http import JsonResponse
import json

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class TaskView(View):
    def post(self, request):
        print(request.POST)
        x = request.POST.get("x")
        y = request.POST.get("y")
        result = add.send(1, 8)
        return JsonResponse({"status": str(result)})


@method_decorator(csrf_exempt, name="dispatch")
class EmailUpdateView(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        user_id = data.get("user_id")
        email = data.get("email")
        result = user_update_email.send(user_id=user_id, email=email)
        return JsonResponse({"status": str(result)})


@method_decorator(csrf_exempt, name="dispatch")
class CreateUserView(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        username = data.get("username") + "_" + str(User.objects.count())
        email = data.get("email")
        password = data.get("password")
        result = create_user.send(username, email, password)
        return JsonResponse({"status": str(result)})


class ListUsersView(View):
    def get(self, request):
        users = User.objects.all()

        return JsonResponse(
            {
                "status": [
                    {"username": user.username, "email": user.email} for user in users
                ]
            }
        )
