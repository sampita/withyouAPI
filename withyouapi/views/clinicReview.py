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
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for a single clinic review

        Returns:
            Response -- JSON serialized clinic review instance
        """
        try:
            clinicreview = ClinicReview.objects.get(pk=pk)
            serializer = ClinicReviewSerializer(clinicreview, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized clinic review instance
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
    
    def update(self, request, pk=None):
        """Handle PUT requests for a clinic review

        Returns:
            Response -- Empty body with 204 status code
        """
        review = ClinicReview.objects.get(pk=pk)
        review.clinic_id = request.data["clinic_id"]
        review.rating = request.data["rating"]
        review.review = request.data["review"]
        review.created_at = request.data["created_at"]
        review.updated_at = request.data["updated_at"]
        review.created_by = request.data["created_by"]
        review.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a clinic review

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            clinicreview = ClinicReview.objects.get(pk=pk)
            clinicreview.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ClinicReview.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
