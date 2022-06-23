from account.models import User,Profile
from rest_framework import serializers
from django.contrib.auth import authenticate



class Userloginserilizer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=64, write_only=True, required=True)
    password = serializers.CharField(min_length=6, max_length=64, write_only=True, required=True)

    def login(self, **kwargs):
        username = self.validated_data['username']
        password = self.validated_data['password']
        
        user = User.objects.filter(username=username).first()
        print("🚀 ~ file: serializers.py ~ line 14 ~ user", user)
        if not user:
            raise serializers.ValidationError({"message": ["No active account found with the given credentials."]})

        user = authenticate(username=user.username, password=password)
        if not user:
            raise serializers.ValidationError({"message": ["No active account found with the given credentials."]})
        return user



class ProfileloginSerializer(serializers.ModelSerializer):
    model = Profile
    fields = ['user_type']