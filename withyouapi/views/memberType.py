"""View module for handling requests about member types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from withyouapi.models import MemberType


class MemberTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for member types

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = MemberType
        url = serializers.HyperlinkedIdentityField(
            view_name='member_type',
            lookup_field='id'
        )
        fields = ('id', 'url', 'category')


class MemberTypes(ViewSet):
    """Member Types"""
            
    def list(self, request):
        """Handle GET requests to member types resource

        Returns:
            Response -- JSON serialized list of member types
        """
        member_types = MemberType.objects.all()
        serializer = MemberTypeSerializer(
            member_types,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)