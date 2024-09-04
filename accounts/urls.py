from django.urls import path
from ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import signup, homepage
from .views import UserInfoView, FamilyMembersView


@method_decorator(ratelimit(key='user', rate='5/m', method='POST', block=True), name='post')
class RateLimitedTokenObtainPairView(TokenObtainPairView):
    pass

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', RateLimitedTokenObtainPairView.as_view(), name='login'),  # Use JWT login view
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-info/', UserInfoView.as_view(), name='user_info'),
    path('family-members/', FamilyMembersView.as_view(), name='family_members'),  # Add this line
    path('', homepage, name='homepage'),
]
