from rest_framework import serializers
from . models import userregister
class userregisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= userregister
        fields = ('id','username', 'firstname', 'lastname', 'email', 'gender', 'phone_number')