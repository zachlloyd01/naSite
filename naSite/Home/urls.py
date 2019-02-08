from django.urls import path, include
from . import views
from .models import NewsFeed

app_name = "Home"

urlpatterns = [
	path('', views.HomePage, name="HomePage"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),
    path('forums/', views.comment_page, name="comment"),
    path('newcomment/', views.create_comment, name="newcomment"),
    path('account/', views.account_page, name="account"),
    path('password-reset/', views.password_reset, name="passwordreset"),
    path('app/', views.application, name="application"),
]
