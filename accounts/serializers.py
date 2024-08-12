from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'first_name', 'last_name', 'birthday',
                  'gender', 'height', 'weight', 'is_family_head')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user instance, with hashed password
        user = CustomUser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birthday=validated_data['birthday'],
            gender=validated_data['gender'],
            height=validated_data['height'],
            weight=validated_data['weight'],
            is_family_head=validated_data.get('is_family_head', False)
        )
        user.set_password(validated_data['password'])  # Hashes the password
        user.save()
        return user

    def update(self, instance, validated_data):
        # Update user instance with hashed password
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
