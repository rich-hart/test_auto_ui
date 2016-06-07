from django.conf.urls import include, url
from rest_framework import routers

from .views import PDFViewSet, CVTestViewSet, OptionViewSet

router = routers.DefaultRouter()

router.register(r'pdfs',PDFViewSet)
router.register(r'options', OptionViewSet)
router.register(r'cvtests', CVTestViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
