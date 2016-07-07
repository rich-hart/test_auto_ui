from rest_framework import serializers
from inspection.models import PDF, CVTest, Option


class PDFSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PDF
        fields = ('id', 'pdf_file',)

class OptionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Option
        fields = ('id', 'name', 'option_string',)


class CVTestSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='result-highlight', format='html')
    class Meta:
        model = CVTest
        fields = ('id',
                  'pdf_a',
                  'pdf_b',
                  'options',
                  'test_created',
                  'results',
                  'highlight',)
        read_only_fields = ('results','test_created')
