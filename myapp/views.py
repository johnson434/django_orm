from os import register_at_fork
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from myapp.models import User


@csrf_exempt
def get_all(reqeuest):
    users = User.objects.all().values("id", "name")
    return JsonResponse(list(users), status=200, safe=False)


@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        user = User.objects.create(
            name=request.POST.get("name"), registerd_at=date.today()
        )
        return JsonResponse(
            {
                "id": user.id,
                "name": user.name,
                "message": f"user {user.name} is created.",
            },
            status=200,
        )

    return JsonResponse(status=200)


@csrf_exempt
def get_user(request, user_id):
    if request.method == "GET":
        user = get_object_or_404(User, id=user_id)
        return JsonResponse({"id": user.id, "name": user.name}, status=200)

    return HttpResponse(request)
