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
        instance = serializer.save()
        inspect(instance.id)
#        inspect.delay(instance.id)

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import renderers
class CVTestHighlight(generics.GenericAPIView):
    queryset = CVTest.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        test = self.get_object()
        return Response(test.results)





