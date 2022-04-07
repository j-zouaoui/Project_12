from rest_framework import serializers
from .models import User, SalesContact, SupportContact

class UserSerializer(serializers.ModelSerializer):
    """
    serialize the user
    """
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password',
                  'is_superuser',
                  'is_sales_contact',
                  'is_support_contact']

class UserDetailSerializer(serializers.ModelSerializer):
    """
    serialize the user detail
    """
    class Meta:
        model = User
        fields = '__all__'


class SalesUserSerializer(serializers.ModelSerializer):
    """
    serialize the user
    """
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password']

class SalesContactSerializer(serializers.ModelSerializer):
    """
    serialize the sales contact
    """
    user = SalesUserSerializer()
    class Meta:
        model = SalesContact
        fields = ['user']

    def create(self, validated_data):
        validated_data = validated_data.pop("user")
        validated_data["is_sales_contact"] = True
        user = User.objects.create(**validated_data)
        sales_instance = SalesContact.objects.create(user=user)
        return sales_instance

class SalesContactDetailSerializer(serializers.ModelSerializer):
    """
    serialize the sales contact detail
    """
    user = UserDetailSerializer()
    class Meta:
        model = SalesContact
        fields = ['user']

    def update(self, instance, validated_data):
        user_updated_data = validated_data.pop('user')
        username = user_updated_data["username"]
        User.objects.filter(username=username).delete()
        User.objects.create(user=instance)
        return super().update(instance, user_updated_data)




class SupportContactSerializer(serializers.ModelSerializer):

    user = SalesUserSerializer()
    class Meta:
        model = SalesContact
        fields = ['user']

    def create(self, validated_data):
        validated_data = validated_data.pop("user")
        validated_data["is_support_contact"] = True
        user = User.objects.create(**validated_data)
        support_instance = SupportContact.objects.create(user=user)
        return support_instance


class SupportContactDetailSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()
    class Meta:
        model = SupportContact
        fields = ['user']

