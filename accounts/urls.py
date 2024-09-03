from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import signup, homepage
from .views import UserInfoView, FamilyMembersView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),  # Use JWT login view
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-info/', UserInfoView.as_view(), name='user_info'),
    path('family-members/', FamilyMembersView.as_view(), name='family_members'),  # Add this line
    path('', homepage, name='homepage'),
]
