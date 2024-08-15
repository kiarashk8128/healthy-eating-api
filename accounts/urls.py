from django.urls import path
from .views import signup, login_view, homepage

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('', homepage, name='homepage'),
]
