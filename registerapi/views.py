from account.models import Profile,User
from rest_framework.views import APIView
from registerapi.serializers import UserSerializer,ProfileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileView(APIView):
    def get(self,request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset,many= True)
        return Response(serializer.data,status = status.HTTP_201_CREATED)

        
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)