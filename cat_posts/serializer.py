from rest_framework import serializers
from .models import Cats

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'date_added', 'name', 'image', 'description', 'admin')
        model = Cats