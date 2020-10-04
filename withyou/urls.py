"""withyou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from withyouapi.views import register_user, login_user, Ethnicities, Forms, Members, MemberTypes

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'forms', Forms, 'form')
router.register(r'ethnicities', Ethnicities, 'ethnicity')
router.register(r'members', Members, 'member')
router.register(r'membertypes', MemberTypes, 'member_type')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user),
    path('login/', login_user),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]