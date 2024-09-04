from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

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

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        try:
            validate_password(value)  # This will run all the validators from settings.py
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value

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
