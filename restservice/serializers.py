from rest_framework import serializers
from restservice.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):
    #firstname = serializers.HyperlinkedModelSerializer
    usertype = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ('firstname','lastname','email','dateOfBirth','username','password','gender','usertype')