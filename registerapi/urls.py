from django.urls import path,include
from  registerapi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud',views.UserViewSet , basename= 'user')
# router.register('crud1',views.UserdataViewSet , basename= 'userdata')

urlpatterns = [
    # path('',include(router.urls)),  
    path('register',views.ProfileView.as_view(),name="register"),
]   