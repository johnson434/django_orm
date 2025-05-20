from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.get_all),
    path("<int:user_id>/", views.get_user),
    path("sign_up/", views.sign_up),
]
