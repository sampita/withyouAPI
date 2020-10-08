"""View module for handling requests about cities"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from withyouapi.models import City


class CitySerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for cities

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = City
        url = serializers.HyperlinkedIdentityField(
            view_name='city',
            lookup_field='id'
        )
        fields = ('name','country_id')


class Cities(ViewSet):
    """Cities"""
            
    def list(self, request):
        """Handle GET requests to cities resource

        Returns:
            Response -- JSON serialized list of cities
        """
        cities = City.objects.all()
        serializer = CitySerializer(
            cities,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
