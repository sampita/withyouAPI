from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from withyouapi.models import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Members
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Member
        url = serializers.HyperlinkedIdentityField(
            view_name='member',
            lookup_field='id'
        )
        fields = ('id', 'brith_date', 'last_screening', 'diagnosis_date', 'city_id', 'country_id', 'ethnicity_id', 'member_type_id', 'user_id')


class Members(ViewSet):
    """Members"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single member

        Returns:
             Response -- JSON serialized member instance
        """ 
        try:
            member = Member.objects.get(pk=pk)
            serializer = MemberSerializer(member,
            context = {'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to members resource

        Returns:
             Response -- JSON serialized list of members
        """      
        member = Members.objects.all()

        serializer = MemberSerializer(
            member,
            many = True,
            context={'request':request}
        )

        return Response(serializer.data)