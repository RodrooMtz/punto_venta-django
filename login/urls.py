from django.urls import path

from login.views import LoginFormView, LogoutView


urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]