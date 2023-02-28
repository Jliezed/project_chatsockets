from django.urls import include, path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, \
    PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from user import views

app_name = "user"
urlpatterns = [
    # Login & Logout
    path('login/', LoginView.as_view(template_name="registration/login.html"),
         name="login"),
    path('logout/', LogoutView.as_view(template_name="registration/logout.html"),
         name='logout'),
]
