"""View module for handling requests about cities"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from withyouapi.models import Clinic


class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for clinics

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Clinic
        url = serializers.HyperlinkedIdentityField(
            view_name='clinic',
            lookup_field='id'
        )
        fields = ('name','street_address','city','country','postal_code','created_at','updated_at','created_by','updated_by')


class Clinics(ViewSet):
    """Clinics"""
            
    def list(self, request):
        """Handle GET requests to clinics resource

        Returns:
            Response -- JSON serialized list of clinics
        """
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(
            clinics,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
