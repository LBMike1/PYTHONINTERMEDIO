from rest_framework import serializers
from apps.owner.models import Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'