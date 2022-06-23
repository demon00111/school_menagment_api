from account.models import Profile,User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = User
        fields = ['id','username','email','password']



class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['id','user','gender','mobile_number','hobby','dob','user_type','caption','video']

    def create(self,validate_data):
        print('<><><><><><><><><><><><',validate_data)
        user = validate_data.pop('user')
        print("🚀 ~ file: serializers.py ~ line 20 ~ user", user)
        password = user.pop('password')
        password = make_password(password)
        user_obj = User.objects.create(password=password,**user)
        print("🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀 ~ file: serializers.py ~ line 22 ~ user_obj", user_obj)
        profile = Profile.objects.create(user=user_obj,**validate_data)
        print("🚀 ~ file: serializers.py ~ line 24 ~ profile🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀", profile)
        return profile