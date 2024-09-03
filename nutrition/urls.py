from django.urls import path
from .views import GenerateMenuView,MenuView,GenerateMenusForAllUsersView

urlpatterns = [
    path('generate-menus/', GenerateMenuView.as_view(), name='generate_menus'),
    path('menus/', MenuView.as_view(), name='menus'),
    path('generate-menus-for-all/', GenerateMenusForAllUsersView.as_view(), name='generate-menus-for-all-users'),


]
