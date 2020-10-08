"""View module for handling requests about cities"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from withyouapi.models import ClinicReview


class ClinicReviewSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for clinic reviews

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = ClinicReview
        url = serializers.HyperlinkedIdentityField(
            view_name='clinic_review',
            lookup_field='id'
        )
        fields = ('clinic','rating','review','created_by','created_at','updated_at')


class ClinicReviews(ViewSet):
    """Clinics"""
            
    def list(self, request):
        """Handle GET requests to clinic review resource

        Returns:
            Response -- JSON serialized list of clinic reviews
        """
        clinicsReviews = ClinicReview.objects.all()
        serializer = ClinicReviewSerializer(
            clinicsReviews,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
