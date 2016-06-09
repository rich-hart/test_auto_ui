from rest_framework import serializers
from inspection.models import PDF, CVTest, Option


class PDFSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PDF
        fields = ('pdf_file',)

class OptionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Option
        fields = ('name', 'option_string',)


class CVTestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CVTest
        fields = ('id',
                  'pdf_a',
                  'pdf_b',
                  'options',
                  'test_created',
                  'results',)
        read_only_fields = ('results','test_created')
