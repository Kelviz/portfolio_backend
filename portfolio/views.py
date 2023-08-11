from django.shortcuts import render
from rest_framework import viewsets, pagination
from rest_framework.response import Response
from .models import About, Tag, Work
from .serializers import AboutSerializer, TagSerializer, WorkSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 6  # Number of posts per page
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
    queryset = Work.objects.all()
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        tag_name = self.request.query_params.get('tag')
        if tag_name:
            queryset = self.queryset.filter(tag__name=tag_name)
            # Use paginate_queryset method
            page = self.paginate_queryset(queryset)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            return super().list(request, *args, **kwargs)
