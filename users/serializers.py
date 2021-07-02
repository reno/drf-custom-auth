from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from users.models import CustomUser


class UserListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='users:detail')
    full_name = serializers.SerializerMethodField('get_full_name')

    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'full_name', 'email']

    def get_full_name(self, obj):
        return obj.get_full_name


class UserDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='users:detail')

    class Meta:
        model = CustomUser
        fields = [
            'url',
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'last_login'
        ]
        read_only_fields = ['date_joined', 'last_login']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True, required=True, style={'input_type': 'password'}
    )

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'username',
            'password',
            'password2',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

