from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .menu_generation import generate_menus_for_user,generate_menus_for_all_users
from .models import Menu, FamilyMember
from rest_framework import status


class GenerateMenusForAllUsersView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            generate_menus_for_all_users(user)
            return Response({"message": "Menus generated successfully for all users"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GenerateMenuView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        family_member_id = request.data.get('family_member_id')

        if family_member_id:
            try:
                family_member = FamilyMember.objects.get(id=family_member_id, family_head=user)
                generate_menus_for_user(user, family_member=family_member)
            except FamilyMember.DoesNotExist:
                return Response({"error": "Family member not found"}, status=404)
        else:
            generate_menus_for_user(user)

        return Response({"message": "Menu generated successfully"}, status=200)

class MenuView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        menus = Menu.objects.filter(user=user).select_related('family_member')
        data = []

        for menu in menus:
            item = {
                "menu_data": menu.menu_data,
                "selected": menu.selected,
            }
            if menu.family_member:
                item["family_member"] = {
                    "id": menu.family_member.id,
                    "first_name": menu.family_member.first_name,
                    "last_name": menu.family_member.last_name,
                }
            data.append(item)

        return Response(data)
