from django.test import TestCase
import inspection
import os

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_PDF = 'A.pdf'
class Inspection(TestCase):
    def test_models(self):
        pdf = inspection.models.PDF(pdf_file=os.path.join(TEST_DIR,TEST_PDF))
        pdf.save()
        cv_test = inspection.models.CVTest(pdf_a=pdf,pdf_b=pdf,options='',results='')    
        cv_test.save()


