from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserRegistrationView

app_name = 'accounts'
urlpatterns = [
path(
    'login/',
    auth_views.login,
    {'template_name':'accounts/registration/login.html'},
    name='login'
),
path(
    'logout/',
    auth_views.logout,
    {'template_name':'accounts/registration/logged_out.html'},
    name='logout'
),
path(
    'password-change/',
    auth_views.PasswordChangeView.as_view(template_name='accounts/registration/password_change_form.html'),
    name='password_change'
),
path(
    'password-change/done/',
    auth_views.PasswordChangeDoneView.as_view(template_name='accounts/registration/password_change_done.html'),
    name='password_change_done'
),
path(
    'register/',
    UserRegistrationView.as_view(),
    name='register'
),
path(
    'password-reset/',
    auth_views.PasswordResetView.as_view(template_name='accounts/registration/password_reset.html'),
    name='password_reset',
),
path(
    'password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='accounts/registration/password_reset_done.html'),
    name='password_reset_done',
),
path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='accounts/registration/password_reset_confirm.html'),
    name='password_reset_confirm',
),
path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(template_name='accounts/registration/password_reset_complete.html'),
    name='password_reset_complete'
),
]
