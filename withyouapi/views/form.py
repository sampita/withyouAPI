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
        fields = ('id', 'member_id', 'form_data', 'form_type', 'inserted_at', 'updated_at')
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

    
    # ********* WORKING ********
    
    # def create(self, request, pk, form_type):
    #     """Handle POST operations for forms
    #     Returns:
    #     Response -- JSON serialized form instance
    #     """
    #     current_user = Member.objects.get(user=request.auth.user)
    #     formType = get_object_or_404(Form, form_type=form_type)

    #     try:
    #         open_form = Form.objects.get(member=current_user, form_type=form_type)

    #     except Form.DoesNotExist:
    #         open_form = Form()
    #         open_form.member_id = request.auth.user.member.id
    #         open_form.save()

    #     serializer = FormSerializer(open_form, context={'request': request})

    #     return Response(serializer.data)