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
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized ClinicReview instance
        """
        newreview = ClinicReview()
        newreview.clinic_id = request.data["clinic_id"]
        newreview.rating = request.data["rating"]
        newreview.review = request.data["review"]
        newreview.created_at = request.data["created_at"]
        newreview.updated_at = request.data["updated_at"]
        newreview.created_by = request.data["created_by"]
        newreview.save()

        serializer = ClinicReviewSerializer(newreview, context={'request': request})

        return Response(serializer.data)
