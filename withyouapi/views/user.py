from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Users
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='user',
            lookup_field='id'
        )
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'is_active', 'date_joined', 'last_login')


class Users(ViewSet):
    """Users"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single user

        Returns:
             Response -- JSON serialized user instance
        """ 
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user,
            context = {'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to users resource

        Returns:
             Response -- JSON serialized list of users
        """      
        user = User.objects.all()

        serializer = UserSerializer(
            user, many = True, context={'request':request})

        return Response(serializer.data)