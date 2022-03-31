from rest_framework import serializers

from .models import IllustratedGuide


class IllustratedGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = IllustratedGuide
        fields = ('number', 'name', 'mon_type', 'height', 'weight', 'thumbnail', 'full_image')
