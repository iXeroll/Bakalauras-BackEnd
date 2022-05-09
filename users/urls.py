from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, GetUser

app_name = "users"

urlpatterns = [
    path("register/", CustomUserCreate.as_view(), name="create_user"),
    path("logout/blacklist/", BlacklistTokenUpdateView.as_view(), name="blacklist"),
    path("u/<str:pk>", GetUser.as_view(), name="user_data"),
]
