from django.shortcuts import render
from rest_framework import viewsets
from inspection.models import PDF, CVTest
from .serializers import PDFSerializer, CVTestSerializer

class PDFViewSet(viewsets.ModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

class CVTestSerializer(viewsets.ModelViewSet):
    queryset = CVTest.objects.all()
    serializer_class = CVTestSerializer
