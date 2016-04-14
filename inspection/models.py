from django.db import models

class PDF(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')

class CVTest(models.Model):
    pdf_a = models.ForeignKey('PDF',related_name='pdf_a')
    pdf_b = models.ForeignKey('PDF',related_name='pdf_b')
    options = models.CharField(max_length=255)
    results = models.TextField()

