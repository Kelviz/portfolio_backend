from rest_framework import serializers
from .models import About, Tag, Work, Skill, Year, Experience, Testimonial, Contact


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


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = ['id', 'name', 'company', 'description']


class YearSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(
        many=True, read_only=True, source='experience_set')

    class Meta:
        model = Year
        fields = ['id', 'year', 'experiences']


class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimonial
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
