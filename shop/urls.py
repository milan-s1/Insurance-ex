from django.urls import path
from . import views
urlpatterns=[
    path('',views.main,name='main'),
    path('login_in',views.login_in,name='login_in'),
    path('main.html',views.main,name='main'),
    path("registration", views.registration, name="registration"),
    path("login", views.login, name="login"),
    path("logout",views.logout,name="logout"),
    path("about_us",views.about_us, name='about_us'),
    path("buy_policies",views.buy_policies, name='buy_policies'),
    path("feedyback", views.feedyback,name='feedyback')
]
