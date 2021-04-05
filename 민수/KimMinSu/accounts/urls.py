from django.urls import path
from . import SignUpView # , SignInView

urlpatterns = [
    path('/signup',SignUpView.as_view()),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'), 
]