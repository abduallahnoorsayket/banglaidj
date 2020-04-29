from rest_framework import serializers
from rest_framework.authtoken.models import Token



from .models import  JWTPayloadTrack



class JWTPayloadTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = JWTPayloadTrack
        fields = '__all__'