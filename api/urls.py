from django.conf.urls import include, url
from rest_framework import routers

from .views import PDFViewSet, CVTestSerializer

router = routers.DefaultRouter()

router.register(r'pdfs',PDFViewSet)
router.register(r'cvtests',CVTestSerializer)

urlpatterns = [
    url(r'^', include(router.urls)),
]
