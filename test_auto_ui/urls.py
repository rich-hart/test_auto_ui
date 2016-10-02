"""test_auto_ui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from api import urls as api_urls
from django.conf import settings
from django.conf.urls.static import static
import rest_framework
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response
from rest_framework import schemas
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from django.contrib.auth import views as auth_views


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Computer Vision API')
    return response.Response(generator.get_schema(request=request))

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#    url(r'^accounts/login/$', auth_views.login),
    url(r'^api/', include(api_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', schema_view),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
