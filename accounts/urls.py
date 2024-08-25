from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import signup, homepage

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),  # Use JWT login view
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', homepage, name='homepage'),
]
