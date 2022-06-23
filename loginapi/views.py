from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import User,Profile
 
from loginapi.serializers import Userloginserilizer,ProfileloginSerializer



class UserloginView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAdminUser]
    serializer = Userloginserilizer
    def post(self,request):
      print('-----------------------------------',request.data)
      serializer = self.serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.login()
      queryset = Profile.objects.all()
      #   logindata = User.objects.all()
      #   serializer_class = ProfileloginSerializer
      #   serializer = Userloginserilizer(data=request.data)

      #   print("????????????????????????????",request.data['username'])
      #   for i in logindata:
      #    i.username == request.data['username'] and i.password == request.data['password']
      # serializer = Userloginserilizer(data=queryset)
   
      return Response("Hello Teacher",status = status.HTTP_201_CREATED)

