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
        fields = ('name','street_address', 'street_address_2', 'city_id','country_id','postal_code','created_at','updated_at','created_by','updated_by', 'is_validated')


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

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Clinic instance
        """

        newclinic = Clinic()
        newclinic.name = request.data["name"]
        newclinic.street_address = request.data["street_address"]
        newclinic.street_address_2 = request.data["street_address_2"]
        newclinic.city_id = request.data["city_id"]
        newclinic.country_id = request.data["country_id"]
        newclinic.postal_code = request.data["postal_code"]
        newclinic.created_at = request.data["created_at"]
        newclinic.updated_at = request.data["updated_at"]
        newclinic.created_by = request.data["created_by"]
        newclinic.updated_by = request.data["updated_by"]
        newclinic.is_validated = request.data["is_validated"]
        newclinic.save()

        serializer = ClinicSerializer(newclinic, context={'request': request})

        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """Handle PUT requests for a Clinic

        Returns:
            Response -- Empty body with 204 status code
        """
        clinic = Clinic.objects.get(pk=pk)
        clinic.name = request.data["name"]
        clinic.street_address = request.data["street_address"]
        clinic.street_address_2 = request.data["street_address_2"]
        clinic.city_id = request.data["city_id"]
        clinic.country_id = request.data["country_id"]
        clinic.postal_code = request.data["postal_code"]
        clinic.created_at = request.data["created_at"]
        clinic.updated_at = request.data["updated_at"]
        clinic.created_by = request.data["created_by"]
        clinic.updated_by = request.data["updated_by"]
        clinic.is_validated = request.data["is_validated"]
        clinic.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)