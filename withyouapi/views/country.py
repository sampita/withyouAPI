"""View module for handling requests about cities"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from withyouapi.models import Country


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for country

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Country
        url = serializers.HyperlinkedIdentityField(
            view_name='country',
            lookup_field='id'
        )
        fields = ('name')


class Countries(ViewSet):
    """Cities"""
            
    def list(self, request):
        """Handle GET requests to cities resource

        Returns:
            Response -- JSON serialized list of cities
        """
        countries = Country.objects.all()
        serializer = CountrySerializer(
            countries,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
