from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import IllustratedGuide
from .serializers import IllustratedGuideSerializer
import random


@api_view(['GET'])
def pokemon_guide(request):
    # illustrated_guide = IllustratedGuide.objects.all().orderby('number')
    illustrated_guide = IllustratedGuide.objects.all()
    serializer = IllustratedGuideSerializer(illustrated_guide, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def pokemon_guide_detail(request, pokemon_id):
    illustrated_guide = IllustratedGuide.objects.filter(id=pokemon_id)
    # illustrated_guide = IllustratedGuide.objects.get(pk=pokemon_id)
    serializer = IllustratedGuideSerializer(illustrated_guide, many=True)
    return Response(serializer.data)
