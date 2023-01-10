
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.home, name="Home"),
    path("Show_Article/<str:pk>", views.show_article, name="Show_article"),
    path("Login", views.login_page, name="Login"),
    path("logout", views.logout_page, name="Logout"),
    path("about/<str:pk>", views.about, name="About"),
    path("Signup", views.signup, name="Signup"),
]
