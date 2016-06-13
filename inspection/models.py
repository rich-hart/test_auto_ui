from django.db import models
import ntpath
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from os.path import join
fs = FileSystemStorage(location=join(settings.MEDIA_ROOT,'pdf'))

class PDF(models.Model):
    pdf_file = models.FileField(upload_to=join(settings.MEDIA_ROOT,'pdf'))
    def __str__(self):
        return ntpath.basename(self.pdf_file.name)
        
class Option(models.Model):
    name = models.CharField(max_length=128)
    option_string = models.CharField(max_length=256, null=True)
     
    def __str__(self):
        return self.name

class CVTest(models.Model):
    pdf_a = models.ForeignKey('PDF',related_name='pdf_a')
    pdf_b = models.ForeignKey('PDF',related_name='pdf_b')
    options = models.ForeignKey('Option')
    test_created = models.DateTimeField(auto_now_add=True)
    results = models.TextField()

