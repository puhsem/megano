from django.urls import path

from .views import sign_in, sign_out, sign_up, user_profile, user_password, user_avatar

urlpatterns = [
    path('sign-in/', sign_in, name='sign_in'),
    path('sign-out/', sign_out, name='sign_out'),
    path('sign-up/', sign_up, name='sign_up'),
    path('profile/', user_profile, name='user_profile'),
    path('profile/password/', user_password, name='user_password'),
    path('profile/avatar/', user_avatar, name='user_avatar'),
]
