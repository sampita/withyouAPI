"""View module for handling requests about forms"""
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from withyouapi.models import Form, Member


class FormSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for forms

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Form
        url = serializers.HyperlinkedIdentityField(
            view_name='form',
            lookup_field='id'
        )
        fields = ('id', 'member_id', 'form_data', 'form_type', 'created_at', 'updated_at')
        depth = 2


class Forms(ViewSet):
    """Forms"""

    def retrieve(self, request, pk=None):
        """Handle get request for a single form
        Returns:
            Response -- JSON serialized form instance
        """

        try:
            form = Form.objects.get(pk=pk)
            serializer = FormSerializer(form, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized form instance
        """

        current_user = Member.objects.get(user=request.auth.user)

        newform = Form()
        newform.member_id = current_user
        newform.form_data = request.data["form_data"]
        newform.form_type = request.data["form_type"]
        newform.created_at = request.data["created_at"]
        newform.updated_at = request.data["updated_at"]
        newform.save()

        serializer = FormSerializer(newform, context={'request': request})

        return Response(serializer.data)