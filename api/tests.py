from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inspection.models import PDF, Option, CVTest
from django.contrib.auth.models import User, Group
import json
from django.conf import settings

class CVTests(APITestCase):
     fixtures = ['fixture.yaml']
     def test_computer_vision_diagnostic(self):
        """
        Ensure we can create a new account object.
        """
        user = User.objects.create_user(
            username='tester', email='u@d.com', password='tester',is_staff=True)


        self.client.login(username='tester',password='tester')  
        url = reverse('pdf-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PDF.objects.count(), 6)
        pdf_list = json.loads(response.content.decode(response.charset))

        url = reverse('option-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Option.objects.count(), 2)

        url = reverse('cvtest-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CVTest.objects.count(), 0)

        pdf_a = PDF.objects.get(pk=1)
        pdf_b = PDF.objects.get(pk=2)
        option = Option.objects.get(pk=1)
 
        data = {
        "pdf_a": "http://127.0.0.1:8001/api/pdfs/1/",
        "pdf_b": "http://127.0.0.1:8001/api/pdfs/1/",
        "options": "http://127.0.0.1:8001/api/options/1/",
        }         
        url = reverse('cvtest-list')
        with self.settings( ENABLE_WORKER_QUEUE = False):
            response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        cv_test = json.loads(response.content.decode(response.charset))
        self.assertSetEqual(set(cv_test.keys()),{'highlight',
                                                 'pdf_a',
                                                 'pdf_b',
                                                 'id',
                                                 'options',
                                                 'results',
                                                 'finished',
                                                 'started',
                                                 'created',})
        self.assertEqual(CVTest.objects.count(), 1)
        cv_test = CVTest.objects.all()[0]
        self.assertEqual(cv_test.results,'Error ox_inspect executable missing.\n'
                                    'Make sure https://github.com/rich-hart/inspection is installed')        

