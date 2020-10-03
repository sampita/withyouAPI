from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from withyouapi.models import Member
from rest_framework.decorators import action


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
        fields = ('id', 'birth_date', 'last_screening', 'diagnosis_date', 'street_address', 'street_address_2', 'postal_code', 'city_id', 'country_id', 'ethnicity_id', 'member_type_id', 'user_id')


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
    
    #Custom action to update user profile
    # @action(methods=['put'], detail=False)
    # def profile_update(self, request):
    #     """
    #     Handle PUT requests for a member
    #     Returns:
    #         Response -- Empty body with 204 status code
    #     """
    #     member = Member.objects.get(pk=request.auth.user.member.id)
    #     member.street_address = request.data["street_address"]
    #     member.street_address_2 = request.data["street_address_2"]
    #     member.postal_code = request.data["postal_code"]
    #     member.city_id = request.data["city_id"]
    #     member.country_id = request.data["country_id"]
    #     member.user.first_name = request.data["first_name"]
    #     member.user.last_name = request.data["last_name"]
    #     member.save()
    #     member.user.save()
    #     return Response({}, status=status.HTTP_204_NO_CONTENT)