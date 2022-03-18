from rest_framework import serializers
from .models import *

class querySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('query',)