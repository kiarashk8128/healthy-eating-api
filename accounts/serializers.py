from rest_framework import serializers
from .models import CustomUser, Family, FamilyMember


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = ['first_name', 'last_name', 'birthday', 'gender', 'height', 'weight']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    family_members = FamilyMemberSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'birthday', 'gender', 'height', 'weight', 'is_family_head', 'family_members']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        family_members_data = validated_data.pop('family_members', [])
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            birthday=validated_data.get('birthday'),
            gender=validated_data.get('gender'),
            height=validated_data.get('height'),
            weight=validated_data.get('weight'),
            is_family_head=validated_data.get('is_family_head', False)
        )
        user.set_password(validated_data['password'])  # Hashes the password
        user.save()

        if user.is_family_head:
            family = Family.objects.create(head=user)
            for member_data in family_members_data:
                FamilyMember.objects.create(family=family, **member_data)

        return user
