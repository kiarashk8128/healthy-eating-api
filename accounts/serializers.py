from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, FamilyMember


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = ['first_name', 'last_name', 'birthday', 'gender', 'height', 'weight']


class CustomUserSerializer(serializers.ModelSerializer):
    family_members = FamilyMemberSerializer(many=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'birthday', 'gender', 'height', 'weight',
                  'is_family_head', 'family_members']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        family_members_data = validated_data.pop('family_members', [])
        user = CustomUser.objects.create_user(**validated_data)
        if user.is_family_head:
            for member_data in family_members_data:
                FamilyMember.objects.create(family_head=user, **member_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid username or password")
        else:
            raise serializers.ValidationError("Must include both username and password")

        data['user'] = user
        return data
