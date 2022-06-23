from django.urls import path,include
from  loginapi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud',views.UserloginView , basename= 'user')
# router.register('crud1',views.UserdataViewSet , basename= 'userdata')

urlpatterns = [
    # path('',include(router.urls)),  
    path('loginapi',views.UserloginView.as_view(),name="loginapi"),
    path('auth/',include('rest_framework.urls', namespace='rest_framework'))
]       