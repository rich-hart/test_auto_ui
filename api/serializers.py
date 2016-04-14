from rest_framework import serializers
from inspection.models import PDF, CVTest
class PDFSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PDF
        fields = ('id', 'pdf_file',)


class CVTestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CVTest
        fields = ('pdf_a',
                  'pdf_b',
                  'options',
                  'results',)
