from rest_framework import serializers
from django.db import models
from .models import Music

class musicSerializer(serializers.ModelSerializer):

    class Meta:
        model=Music
        fields= '__all__'

