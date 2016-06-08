from django.shortcuts import render
from rest_framework import viewsets
from inspection.models import PDF, CVTest, Option
from .serializers import PDFSerializer, CVTestSerializer, OptionSerializer
from inspection.tasks import inspect

class PDFViewSet(viewsets.ModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class CVTestViewSet(viewsets.ModelViewSet):
    queryset = CVTest.objects.all()
    serializer_class = CVTestSerializer

    def perform_create(self, serializer):
        pdf_a_url = self.request.data['pdf_a']
        pdf_b_url = self.request.data['pdf_b']
        options = self.request.data['options']
        inspect.delay(pdf_a_url,
                      pdf_b_url,
                      options)
        serializer.save()
