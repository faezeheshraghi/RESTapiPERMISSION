from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import Register, Logout,login,Page

urlpatterns = [
    path('login/', login),
    path('logout/', Logout.as_view()),
    path('register/', Register.as_view()),
    path('login/page/', Page.as_view()),
]
