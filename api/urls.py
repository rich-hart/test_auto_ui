from django.conf.urls import include, url
from rest_framework import routers

from .views import (
    PDFViewSet, 
    CVTestViewSet, 
    OptionViewSet,
    UserViewSet,
    GroupViewSet,
    CVTestHighlight,
)

router = routers.DefaultRouter()

router.register(r'users',UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'pdfs', PDFViewSet)
router.register(r'options', OptionViewSet)
router.register(r'cvtests', CVTestViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^cvtests/(?P<pk>[0-9]+)/highlight/$',CVTestHighlight.as_view(),name='result-highlight'),
]
