from django.shortcuts import render
from rest_framework import viewsets
from inspection.models import PDF, CVTest, Option
from django.contrib.auth.models import User, Group
from .serializers import (
    PDFSerializer, 
    CVTestSerializer, 
    OptionSerializer,
    UserSerializer,
    GroupSerializer,
)
from inspection.tasks import inspect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import renderers
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAuthenticatedOrReadOnly,
)
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @list_route()
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-last_login')
        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)

class PDFViewSet(viewsets.ModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )

class CVTestViewSet(viewsets.ModelViewSet):
    queryset = CVTest.objects.all()
    serializer_class = CVTestSerializer
    if not settings.DEMO:
        permission_classes = (
            IsAuthenticatedOrReadOnly,
        )
    
    def perform_create(self, serializer):
        instance = serializer.save()
        if settings.ENABLE_WORKER_QUEUE:
            inspect.delay(instance.id)
        else:
            inspect(instance.id)

class CVTestHighlight(generics.GenericAPIView):
    queryset = CVTest.objects.all()
    renderer_classes = (renderers.TemplateHTMLRenderer,)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )

    def get(self, request, *args, **kwargs):
        test = self.get_object()
        if test.results:
            return Response({'results':test.results},template_name="results.html")
        else:
            return Response({'results':'Pending...'},template_name="results.html")
