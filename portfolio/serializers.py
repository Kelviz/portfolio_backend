from rest_framework import serializers
from .models import About, Tag, Work


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = '__all__'
