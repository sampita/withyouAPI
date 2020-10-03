"""View module for handling requests about ethnicities"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from withyouapi.models import Ethnicity


class EthnicitySerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for ethnicities

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Ethnicity
        url = serializers.HyperlinkedIdentityField(
            view_name='ethnicity',
            lookup_field='name'
        )
        fields = ('id', 'url', 'name')


class Ethnicities(ViewSet):
    """Ethnicities"""
            
    def list(self, request):
        """Handle GET requests to ethnicities resource

        Returns:
            Response -- JSON serialized list of ethnicities
        """
        ethnicities = Ethnicity.objects.all()
        serializer = EthnicitySerializer(
            ethnicities,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)