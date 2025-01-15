# serializers.py
from rest_framework import serializers
from .models import HackathonIdea

class HackathonIdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonIdea
        fields = ['id', 'name', 'description', 'build_approach', 'created_at']
