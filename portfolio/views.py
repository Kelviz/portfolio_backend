from django.shortcuts import render
from rest_framework import viewsets, pagination
from rest_framework.response import Response
from .models import About, Tag, Work, Skill, Year, Experience, Testimonial, Contact
from .forms import ContactForm
from .serializers import AboutSerializer, TagSerializer, WorkSerializer, SkillSerializer, YearSerializer, TestimonialSerializer, ContactSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 3  # Number of posts per page
    page_size_query_param = 'page_size'
    max_page_size = 100


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WorkSerializer
    queryset = Work.objects.all().order_by('id')
    #pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        tag_name = self.request.query_params.get('tag')
        if tag_name:
            queryset = self.queryset.filter(tag__name=tag_name)
            # Use paginate_queryset method
            #page = self.paginate_queryset(queryset)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return super().list(request, *args, **kwargs)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class YearExperienceViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class SendMessageViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def create(self, request):
        form = ContactForm(request.data)

        if form.is_valid():
            contact = Contact(
                name=form.cleaned_data['name'],
                message=form.cleaned_data['message'],
                email=form.cleaned_data['email'],

            )

            contact.save()
            serializer = self.get_serializer(contact)
            return Response(serializer.data)
        else:
            return Response(form.errors, status=400)
