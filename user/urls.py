from django.urls import path
from user.views import (
    CreateUserView,
    CreateTokenView,
    ManageUserView,
    ObtainAuthTokenEmail
)


app_name = "user"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("api/token/", ObtainAuthTokenEmail.as_view(), name="api_token_email"),
]
